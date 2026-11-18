"""Generate transcript Excel from video audio; never read the supplied transcript."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

import imageio_ffmpeg
from openpyxl import load_workbook
from workbook_io import write_workbook

VERSION = 'audio-transcripts-1'

def video_context(video):
    stem = re.sub(r'-\d{4}-\d{2}-\d{2}_Video$', '', video.stem)
    parts = stem.split('-')
    date = re.search(r'(\d{4}-\d{2}-\d{2})_Video$', video.stem)
    return dict(Q1_4=parts[-1] if len(parts)>1 else '', Q1_6=' '.join(parts[:-1]) if len(parts)>1 else stem,
                RecordedDate=date.group(1) if date else '', Identity_Source='Video filename')

def transcribe_video(client, video, cache_dir, model='gpt-transcribe', chunk_seconds=600):
    if chunk_seconds <= 0 or chunk_seconds > 1800:
        raise ValueError('chunk_seconds must be between 1 and 1800')
    video = Path(video)
    hasher = hashlib.sha256()
    with video.open('rb') as handle:
        for block in iter(lambda:handle.read(1024*1024), b''):hasher.update(block)
    identity = dict(version=VERSION, video_sha256=hasher.hexdigest(), model=model, chunk_seconds=chunk_seconds)
    key = hashlib.sha256(json.dumps(identity,sort_keys=True).encode()).hexdigest()[:24]
    folder = Path(cache_dir)/key
    folder.mkdir(parents=True,exist_ok=True)
    final = folder/'transcript.json'
    if final.exists():return dict(json.loads(final.read_text()), video_filename=video.name)
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    # Bounded chunks at 48 kbps stay comfortably below the API upload limit.
    subprocess.run([ffmpeg,'-hide_banner','-loglevel','error','-i',str(video),'-map','0:a:0','-vn',
                    '-ac','1','-ar','16000','-c:a','libmp3lame','-b:a','48k','-f','segment',
                    '-segment_time',str(chunk_seconds),'-reset_timestamps','1','-y',str(folder/'audio-%03d.mp3')],
                   check=True,capture_output=True)
    chunks=[]
    paths=sorted(folder.glob('audio-*.mp3'))
    if not paths:raise ValueError(f'No audio decoded from {video.name}')
    for i,path in enumerate(paths):
        cached=path.with_suffix('.json')
        if cached.exists():result=json.loads(cached.read_text())
        else:
            if path.stat().st_size >= 25_000_000:raise ValueError('Audio chunk exceeds API upload limit')
            print(f'Transcribing {video.name}: chunk {i+1}/{len(paths)}',flush=True)
            with path.open('rb') as handle:
                response=client.audio.transcriptions.create(model=model,file=handle)
            text=response.text.strip()
            if not text:raise ValueError(f'Empty transcription for {video.name} chunk {i+1}')
            result=dict(chunk_index=i, approximate_start_seconds=i*chunk_seconds,text=text)
            cached.write_text(json.dumps(result,ensure_ascii=False,indent=2))
        chunks.append(result)
    result=dict(identity,video_filename=video.name,text='\n\n'.join(c['text'] for c in chunks),chunks=chunks)
    final.write_text(json.dumps(result,ensure_ascii=False,indent=2))
    return result

def generate_transcript_workbook(client,videos,target,model='gpt-transcribe',preview_dir=None):
    videos=list(videos)
    if not videos:raise ValueError('No videos to transcribe')
    if len({p.name for p in videos})!=len(videos):raise ValueError('Video filenames must be unique to match transcripts safely')
    target=Path(target);target.parent.mkdir(parents=True,exist_ok=True)
    rows=[];manifest=[]
    headers=['Video','Response ID','First Name','Last Name','Recorded Date','Transcript','Transcription Model','Transcript File','Identity Source']
    for video in videos:
        result=transcribe_video(client,video,target.parent/'audio_cache',model)
        context=video_context(video)
        text_path=target.parent/(video.stem+'.transcript.txt')
        text_path.write_text(result['text']+'\n')
        rows.append([video.name,'ASR_'+result['video_sha256'][:16],context['Q1_4'],context['Q1_6'],context['RecordedDate'],
                     result['text'],model,text_path.name,context['Identity_Source']])
        manifest.append(dict(result,context=context))
    write_workbook(target,[dict(name='Transcriptions',headers=headers,rows=rows,previewRange='A1:E3')],preview_dir)
    target.with_suffix('.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    return target

def load_transcript_workbook(path, videos):
    """Read the generated file back; downstream text must originate here."""
    wb=load_workbook(path,read_only=True,data_only=True)
    try:
        values=iter(wb['Transcriptions'].values);headers=next(values)
        aliases={'Response ID':'ResponseId','First Name':'Q1_4','Last Name':'Q1_6','Recorded Date':'RecordedDate','Transcript':'Q14_Video_Transcript','Transcription Model':'Transcription_Model','Transcript File':'Transcript_File','Identity Source':'Identity_Source'}
        headers=[aliases.get(h,h) for h in headers]
        records={}
        for row in values:
            aliases={'Response ID':'ResponseId','First Name':'Q1_4','Last Name':'Q1_6','Recorded Date':'RecordedDate','Transcript':'Q14_Video_Transcript','Transcription Model':'Transcription_Model','Transcript File':'Transcript_File','Identity Source':'Identity_Source'}
            record={aliases.get(key,key):value for key,value in zip(headers,row)};name=record['Video']
            if name in records:raise ValueError('Duplicate video in generated transcript workbook')
            if not str(record.get('Q14_Video_Transcript') or '').strip():raise ValueError(f'Missing generated transcript: {name}')
            records[name]=record
    finally:wb.close()
    expected={video.name for video in videos}
    if expected!=set(records):raise ValueError('Generated workbook does not match the input video set')
    return records

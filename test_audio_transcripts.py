from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch
import json
import unittest
from openpyxl import load_workbook
from audio_transcripts import transcribe_video, generate_transcript_workbook, load_transcript_workbook, video_context
from workbook_io import entity_columns


class AudioTranscriptTests(unittest.TestCase):
    def test_entity_columns_are_semicolon_text_not_json(self):
        fields=entity_columns(dict(people=['Juan Reyes Sierra','George W. Bush'],themes=['Family memory','Presidential visit'],perspective='Inherited account'))
        self.assertEqual(fields['people'],'Juan Reyes Sierra; George W. Bush')
        self.assertEqual(fields['themes'],'Family memory; Presidential visit')
        self.assertEqual(fields['perspective'],'Inherited account')
        self.assertEqual(fields['dates'],'')
        self.assertNotIn('"',fields['people'])
        quoted=entity_columns(dict(people=['Speaker called “Donna”','"Danna"']))
        self.assertEqual(quoted['people'],'Speaker called Donna; Danna')

    def test_filename_context_preserves_compound_last_name(self):
        c=video_context(Path('Arrieta-Ventura-Danna-2026-09-11_Video.mp4'))
        self.assertEqual((c['Q1_4'],c['Q1_6']),('Danna','Arrieta Ventura'))
        self.assertEqual(c['RecordedDate'],'2026-09-11')

    def test_transcription_is_cached_and_original_workbook_is_not_needed(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp);video=root/'Lundy-Ken-2026-09-11_Video.mp4';video.write_bytes(b'video fixture')
            calls=[]
            def fake_audio(*args,**kwargs):
                pattern=Path(args[0][-1]);(pattern.parent/'audio-000.mp3').write_bytes(b'audio fixture')
            def fake_transcribe(**kwargs):
                calls.append(kwargs['model'])
                return SimpleNamespace(text='My name is Ken Lundy. This is generated from audio.')
            client=SimpleNamespace(audio=SimpleNamespace(transcriptions=SimpleNamespace(create=fake_transcribe)))
            with patch('audio_transcripts.subprocess.run',side_effect=fake_audio):
                first=transcribe_video(client,video,root/'cache')
                second=transcribe_video(client,video,root/'cache')
                renamed=root/'Same-content-different-name.mp4';renamed.write_bytes(video.read_bytes())
                reused=transcribe_video(client,renamed,root/'cache')
            self.assertEqual(first['text'],second['text'])
            self.assertEqual(calls,['gpt-transcribe'])
            self.assertEqual(reused['video_filename'],renamed.name)

    def test_generated_workbook_is_read_back_without_source_excel(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp);video=root/'Lundy-Ken-2026-09-11_Video.mp4';video.write_bytes(b'fixture')
            generated=dict(text='Actual generated speech text.',video_sha256='a'*64,video_filename=video.name,chunks=[])
            path=root/'generated.xlsx'
            with patch('audio_transcripts.transcribe_video',return_value=generated):
                generate_transcript_workbook(None,[video],path)
            records=load_transcript_workbook(path,[video])
            self.assertEqual(records[video.name]['Q14_Video_Transcript'],generated['text'])
            self.assertEqual(records[video.name]['Transcription_Model'],'gpt-transcribe')
            self.assertEqual((root/(video.stem+'.transcript.txt')).read_text().strip(),generated['text'])
            with self.assertRaises(ValueError):load_transcript_workbook(path,[])


if __name__=='__main__':unittest.main()

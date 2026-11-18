"""Refresh the README example from a generated metadata JSON record (no API calls)."""
import argparse
from html import escape
import json
from pathlib import Path
import re
import subprocess
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audio_transcripts import video_context
from visual_evidence import visual_json

ROOT = Path(__file__).resolve().parents[1]
VIDEO_URL = 'https://github.com/user-attachments/assets/56694318-b34f-448b-ae63-0d945b35f1cf'
START = '<!-- BEGIN EXCEL VIDEO EXAMPLE -->'
END = '<!-- END EXCEL VIDEO EXAMPLE -->'


def listing(value):
    values = value if isinstance(value, list) else [value] if value else []
    return '<ul>' + ''.join('<li>' + escape(str(v)) + '</li>' for v in (values or ['None recorded'])) + '</ul>'


def identity(record):
    context = video_context(Path(record['video_filename']))
    name = ' '.join([context['Q1_4'], context['Q1_6']])
    slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    return name, slug


def build(record, video_url=None):
    name, slug = identity(record)
    facets = record['entities_and_facets']
    left = ''
    for key in ('people', 'locations', 'organizations', 'dates', 'themes', 'perspective'):
        left += '<h4>' + key.title() + '</h4>' + listing(facets.get(key))
    left += '<h4>Visual evidence</h4>'
    observations = record['visual_evidence']['visual_observations']
    for category, label in [('attire_and_symbols', 'Attire and symbols'),
                             ('artifacts_and_props', 'Artifacts and props'),
                             ('activities_and_emotional_moments', 'Activities, expressions and gaze')]:
        left += '<p><strong>' + label + '</strong></p>'
        left += listing([f"{o['timestamp_seconds']:g} s · {o['frame_id']} · {o['observation']} (confidence: {o['confidence']}; review required: {o['review_required']})"
                         for o in observations if o['category'] == category])
    right = '<h3>' + escape(name) + '</h3>'
    right += f"<p>{record['duration_seconds']:.0f} seconds · {record['sampled_frames']} sampled frames</p>"
    if video_url:
        # GitHub renders its uploaded attachment as a native inline video player.
        # Use that player alone instead of also showing a duplicate thumbnail.
        right += '<p>Play/pause and audio controls are available below.</p>\n\n' + video_url + '\n\n'
        right += f'<p><a href="examples/videos/{slug}.mp4">Open video with audio if the inline player is unavailable</a></p>'
    else:
        right += f'<p><a href="examples/videos/{slug}.mp4"><img src="examples/previews/{slug}.jpg" width="480" alt="Play {escape(name)} interview with audio"></a></p>'
        right += f'<p><a href="examples/videos/{slug}.mp4">Open video player with audio</a> · Compressed viewing copy; original duration retained.</p>'
    right += '<h4>Generated description</h4><p>' + escape(record['description']) + '</p>'
    right += '<h4>Keywords</h4>' + listing(record['keywords'])
    right += '<h4>Selected FAST subjects</h4>' + listing(record['fast_subjects'])
    right += '<h4>Review status</h4><p>' + escape(record['quality']['status']) + '</p>'
    right += '<h4>Review issues</h4>' + listing(record['quality'].get('issues'))
    right += '<h4>Uncertainties</h4>' + listing(record.get('uncertainty_notes'))
    candidates = listing([f"{i}. {c['heading']} ({c.get('id', c.get('authority_id', ''))})" for i, c in enumerate(record['fast_candidates'], 1)])
    return (f'### {name}\n\n'
            '<table>\n<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>\n<tr>\n<td width="40%" valign="top">\n\n'
            + left + '\n\n</td>\n<td width="60%" valign="top">\n\n' + right + '\n\n</td>\n</tr>\n</table>\n\n'
            + '<details><summary>Visual evidence JSON</summary>\n\n```json\n' + visual_json(record['visual_evidence']) + '\n```\n\n</details>\n\n'
            + '<details><summary>All retrieved FAST candidates</summary>\n\n' + candidates + '\n\n</details>\n\n'
            + f'[Full generated result and supporting evidence](examples/data/{slug}.json).\n\n')


def prepare_media(record):
    import imageio_ffmpeg
    _, slug = identity(record)
    video = ROOT/'examples/videos'/f'{slug}.mp4'
    preview = ROOT/'examples/previews'/f'{slug}.jpg'
    source = ROOT/'Library-Metadata'/record['video_path']
    video.parent.mkdir(parents=True, exist_ok=True)
    preview.parent.mkdir(parents=True, exist_ok=True)
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    if not video.exists():
        subprocess.run([ffmpeg, '-hide_banner', '-loglevel', 'error', '-i', str(source),
                        '-map', '0:v:0', '-map', '0:a:0', '-vf', 'scale=640:-2',
                        '-c:v', 'libx264', '-preset', 'fast', '-crf', '30', '-pix_fmt', 'yuv420p',
                        '-c:a', 'aac', '-b:a', '64k', '-movflags', '+faststart', '-y', str(video)], check=True)
    if not preview.exists():
        subprocess.run([ffmpeg, '-hide_banner', '-loglevel', 'error', '-ss', '2', '-i', str(video),
                        '-frames:v', '1', '-q:v', '3', '-y', str(preview)], check=True)
    print(f'Prepared {slug}: {video.stat().st_size/1e6:.1f} MB', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=ROOT/'outputs/notebook/UCFremembers911_video_metadata.json')
    parser.add_argument('--video', help='Optional single filename; by default publish all records.')
    parser.add_argument('--prepare-media', action='store_true', help='Create compressed video copies and previews from local source videos.')
    parser.add_argument('--video-url', default=VIDEO_URL)
    args = parser.parse_args()
    records = json.loads(args.input.read_text())
    if args.video:
        records = [r for r in records if r['video_filename'] == args.video]
    if not records:
        raise ValueError('No matching video records.')
    if args.prepare_media:
        for record in records:
            prepare_media(record)
    # Publish metadata only; omit full transcript spans and private workbook context.
    keys = ('video_filename', 'duration_seconds', 'sampled_frames', 'description',
            'entities_and_facets', 'visual_evidence', 'keywords', 'fast_subjects',
            'description_support', 'keyword_support', 'fast_selection_details',
            'fast_candidates', 'quality', 'uncertainty_notes', 'frame_manifest')
    folder = ROOT/'examples/data'
    folder.mkdir(parents=True, exist_ok=True)
    for record in records:
        _, slug = identity(record)
        if not (ROOT/'examples/videos'/f'{slug}.mp4').exists():
            raise FileNotFoundError('Run with --prepare-media to create the example videos first.')
        example = {k: record[k] for k in keys if k in record}
        (folder/f'{slug}.json').write_text(json.dumps(example, ensure_ascii=False, indent=2)+'\n')
        if slug == 'ken-lundy':
            (ROOT/'examples/ken-lundy-metadata.json').write_text(json.dumps(example, ensure_ascii=False, indent=2)+'\n')
    index = '\n'.join(f'- [{identity(r)[0]}](#{identity(r)[1]})' for r in records)
    section = (START + '\n## Video examples — all generated results\n\n'
               f'All {len(records)} interviews from the eight-frame notebook run. Each example includes every entity facet, all visual-evidence categories, the JSON evidence, description, five keywords, selected FAST subjects, retrieved candidates, and review notes. '
               'Ken Lundy has one inline video player with play/pause and audio controls. For the other interviews, click the preview or Open video player with audio to open the full MP4 on GitHub. '
               'Values are shown as generated, including unresolved transcription details.\n\n'
               + index + '\n\n' + ''.join(build(r, args.video_url if identity(r)[1] == 'ken-lundy' else None) for r in records)
               + 'Source: `outputs/notebook/UCFremembers911_video_metadata.json`, matching the generated Excel workbook. '
               'Visual observations are retained without post-processing.\n' + END)
    readme = ROOT/'README.md'
    text = readme.read_text()
    start = text.index(START)
    end = text.index(END, start)+len(END)
    readme.write_text(text[:start]+section+text[end:])
    print(f'Updated README and JSON examples for {len(records)} videos.')


if __name__ == '__main__':
    main()

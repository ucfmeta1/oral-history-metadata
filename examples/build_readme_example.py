"""Refresh the README example from a generated metadata JSON record (no API calls)."""
import argparse
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIDEO_URL = 'https://github.com/user-attachments/assets/56694318-b34f-448b-ae63-0d945b35f1cf'
START = '<!-- BEGIN EXCEL VIDEO EXAMPLE -->'
END = '<!-- END EXCEL VIDEO EXAMPLE -->'


def listing(value):
    values = value if isinstance(value, list) else [value] if value else []
    return '<ul>' + ''.join('<li>' + escape(str(v)) + '</li>' for v in (values or ['None recorded'])) + '</ul>'


def build(record, video_url):
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
    right = '<h3>Ken Lundy</h3>'
    right += f"<p>{record['duration_seconds']:.0f} seconds · {record['sampled_frames']} sampled frames</p>"
    right += '<p>Play/pause and audio controls are available in the GitHub video player.</p>\n\n' + video_url + '\n\n'
    right += '<h4>Generated description</h4><p>' + escape(record['description']) + '</p>'
    right += '<h4>Keywords</h4>' + listing(record['keywords'])
    right += '<h4>Selected FAST subjects</h4>' + listing(record['fast_subjects'])
    right += '<h4>Review status</h4><p>' + escape(record['quality']['status']) + '</p>'
    right += '<h4>Review issues</h4>' + listing(record['quality'].get('issues'))
    right += '<h4>Uncertainties</h4>' + listing(record.get('uncertainty_notes'))
    return (START + '\n## Video example: Ken Lundy — all facets\n\n'
            'One generated example from the eight-frame notebook run. All six entity facets and all three visual-evidence categories appear below, including categories with no observations. Values are shown as generated; review flags and transcription uncertainty remain visible.\n\n'
            '<table>\n<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>\n<tr>\n<td width="40%" valign="top">\n\n'
            + left + '\n\n</td>\n<td width="60%" valign="top">\n\n' + right + '\n\n</td>\n</tr>\n</table>\n\n'
            'Source: `outputs/notebook/UCFremembers911_video_metadata.json`, matching the generated Excel workbook. '
            'This is a static metadata panel; the video attachment supports playback with audio. '
            '[Full example, including evidence support and FAST candidates](examples/ken-lundy-metadata.json). '
            'Observations are extracted directly from sampled frames with no post-processing.\n' + END)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=ROOT/'outputs/notebook/UCFremembers911_video_metadata.json')
    parser.add_argument('--video', default='Lundy-Ken-2026-09-11_Video.mp4')
    parser.add_argument('--video-url', default=VIDEO_URL)
    args = parser.parse_args()
    records = json.loads(args.input.read_text())
    matches = [r for r in records if r['video_filename'] == args.video]
    if len(matches) != 1:
        raise ValueError('Expected one matching video record.')
    record = matches[0]
    # Publish metadata only; omit full transcript spans and private workbook context.
    keys = ('video_filename', 'duration_seconds', 'sampled_frames', 'description',
            'entities_and_facets', 'visual_evidence', 'keywords', 'fast_subjects',
            'description_support', 'keyword_support', 'fast_selection_details',
            'fast_candidates', 'quality', 'uncertainty_notes', 'frame_manifest')
    example = {k: record[k] for k in keys if k in record}
    (ROOT/'examples/ken-lundy-metadata.json').write_text(json.dumps(example, ensure_ascii=False, indent=2)+'\n')
    readme = ROOT/'README.md'
    text = readme.read_text()
    start = text.index(START)
    end = text.index(END, start)+len(END)
    readme.write_text(text[:start]+build(record, args.video_url)+text[end:])
    print(f"Updated README and example: {record['sampled_frames']} frames, {len(record['visual_evidence']['visual_observations'])} observations.")


if __name__ == '__main__':
    main()

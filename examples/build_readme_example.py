"""Build the README video panel from one generated Excel row, without API calls."""
import argparse
from html import escape
import json
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
VIDEO_URL = 'https://github.com/user-attachments/assets/56694318-b34f-448b-ae63-0d945b35f1cf'
START = '<!-- BEGIN EXCEL VIDEO EXAMPLE -->'
END = '<!-- END EXCEL VIDEO EXAMPLE -->'

def listing(values, empty='None recorded'):
    return '<ul>' + ''.join('<li>' + escape(str(v)) + '</li>' for v in (values or [empty])) + '</ul>'

def build(workbook, video_name, video_url):
    wb = load_workbook(workbook, read_only=True, data_only=True)
    try:
        rows = iter(wb['Generated_Metadata'].values)
        headers = next(rows)
        matches = [dict(zip(headers, row)) for row in rows if Path(str(row[headers.index('Video')])).name == video_name]
    finally:
        wb.close()
    if len(matches) != 1:
        raise ValueError('Expected exactly one matching video row in Generated_Metadata.')
    row = matches[0]
    visual = json.loads(row['Visual_Evidence_JSON'])
    context = json.loads(row['Workbook_Context_JSON'])
    keywords = row['Keywords'].split('; ')
    fast = row['FAST_Subjects'].split('; ')
    name = ' '.join(str(context.get(k, '')).strip() for k in ('Q1_4', 'Q1_6')).strip()
    left = '<h4>Entities &amp; affiliation</h4>' + listing([name, context.get('Q6', ''), context.get('Q11', '')])
    left += '<h4>Primary subjects</h4>' + listing(row['Primary_Subjects'].split('; '))
    left += '<h4>Themes &amp; secondary subjects</h4>' + listing(row['Secondary_Subjects'].split('; '))
    left += '<h4>Visual evidence: sampled frames</h4>'
    for key, label in [('visible_people', 'Visible people'), ('visible_objects', 'Artifacts & props'),
                       ('activities', 'Observed activities'), ('scenes', 'Scene'), ('onscreen_text', 'Onscreen text')]:
        left += '<p><strong>' + label + '</strong></p>' + listing(visual.get(key, []), 'None detected in sampled frames')
    left += '<h4>Evidence notes</h4>' + listing(json.loads(row['Evidence_Notes']))
    right = '<h3>' + escape(name) + '</h3><p>' + escape(str(context.get('Q11', ''))) + '</p>'
    right += '<p>Showing 1 of 6 oral histories · ' + str(round(row['Duration_Seconds'])) + ' seconds · ' + str(row['Sampled_Frames']) + ' sampled frames</p>'
    right += '<p>Play or pause using the controls below. Use the speaker control to unmute the audio.</p>\n\n' + video_url + '\n\n'
    right += '<h4>Generated description</h4><p>' + escape(row['Description']) + '</p>'
    right += '<h4>Generated keywords</h4>' + listing(keywords)
    right += '<h4>Selected FAST subject headings</h4>' + listing(fast)
    right += '<details><summary>Uncertainties recorded in Excel</summary>' + listing(json.loads(row['Uncertainties'])) + '</details>'
    section = START + '\n## Video example: Ken Lundy\n\n'
    section += 'UCF Remembers 9/11 — sample metadata view. The left panel shows entities, subjects, and visual evidence from the generated Excel row; the right panel shows the matching video and generated description, keywords, and FAST headings.\n\n'
    section += '<table>\n<tr><th width="35%">Entities &amp; evidence</th><th width="65%">Video &amp; generated metadata</th></tr>\n<tr>\n<td width="35%" valign="top">\n\n' + left + '\n\n</td>\n<td width="65%" valign="top">\n\n' + right + '\n\n</td>\n</tr>\n</table>\n\n'
    section += 'Source: `outputs/notebook/UCFremembers911_video_metadata.xlsx`, `Generated_Metadata`, Ken Lundy’s row. Visual evidence comes from sampled frames; observations and subjects are shown as generated. This README panel is static; its video supports playback and audio controls. [View the exported example data](examples/ken-lundy-metadata.json).\n' + END + '\n\n'
    payload = dict(video_filename=video_name, description=row['Description'], keywords=keywords, fast_subjects=fast,
                   primary_subjects=row['Primary_Subjects'].split('; '), secondary_subjects=row['Secondary_Subjects'].split('; '),
                   visual_evidence=visual, workbook_context=context, evidence_notes=json.loads(row['Evidence_Notes']),
                   uncertainty_notes=json.loads(row['Uncertainties']), source_sheet='Generated_Metadata')
    return section, payload

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workbook', type=Path, default=ROOT/'outputs/notebook/UCFremembers911_video_metadata.xlsx')
    parser.add_argument('--video', default='Lundy-Ken-2026-09-11_Video.mp4')
    parser.add_argument('--video-url', default=VIDEO_URL)
    args = parser.parse_args()
    section, payload = build(args.workbook, args.video, args.video_url)
    path = ROOT/'README.md'
    text = path.read_text()
    if START in text:
        start = text.index(START)
        end = text.index(END, start) + len(END)
        text = text[:start] + section.rstrip() + text[end:]
    else:
        start = text.index('## Video example: Ken Lundy')
        end = text.index('## Setup and run', start)
        text = text[:start] + section + text[end:]
    path.write_text(text)
    (ROOT/'examples/ken-lundy-metadata.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
    print('Updated README panel and example JSON from Excel.')

if __name__ == '__main__':
    main()

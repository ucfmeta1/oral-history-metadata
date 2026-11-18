"""Write a technical report from completed robustness outputs; no API calls."""
from collections import Counter
import json
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from openpyxl import load_workbook

ROOT=Path(__file__).resolve().parents[1]

def main():
    source=ROOT/'outputs/notebook/UCFremembers911_video_metadata.json'
    results=json.loads(source.read_text())
    if len(results)!=6 or not all('quality' in r for r in results):
        raise ValueError('Report requires six completed robustness records, not baseline or partial outputs.')
    workbook=load_workbook(source.with_suffix('.xlsx'),read_only=False,data_only=True)
    errors=workbook['Errors'].max_row-1
    if errors:raise ValueError('Resolve execution errors before generating the final report.')
    workbook.close()
    statuses=Counter(r['quality']['status'] for r in results)
    d=Document();section=d.sections[0]
    section.top_margin=section.bottom_margin=Inches(.65)
    section.left_margin=section.right_margin=Inches(.75)
    normal=d.styles['Normal'];normal.font.name='Calibri';normal.font.size=Pt(10.5)
    normal.paragraph_format.space_after=Pt(6)
    for name,size in [('Title',23),('Heading 1',15),('Heading 2',12)]:
        s=d.styles[name];s.font.name='Calibri';s.font.size=Pt(size);s.font.color.rgb=RGBColor.from_string('17365D')
    section.header.paragraphs[0].text='UCF REMEMBERS 9/11 | METADATA ROBUSTNESS'
    footer=section.footer.paragraphs[0];footer.text='November 12, 2026 • Page '
    field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)
    def p(text):d.add_paragraph(text)
    def h(text):d.add_heading(text,level=2)
    def page(text):d.add_page_break();d.add_heading(text,level=1)
    def table(headers,rows):
        t=d.add_table(rows=1,cols=len(headers));t.style='Light Shading Accent 1'
        for c,text in zip(t.rows[0].cells,headers):c.text=str(text)
        for row in rows:
            cells=t.add_row().cells
            for c,text in zip(cells,row):
                c.text=str(text)
                for paragraph in c.paragraphs:
                    paragraph.paragraph_format.space_after=Pt(3)
                    for run in paragraph.runs:run.font.size=Pt(9)
    d.add_heading('More robust video metadata',0)
    d.add_paragraph('Implementation and technical validation report',style='Subtitle')
    p('Collection: UCF Remembers 9/11\nPrepared: November 12, 2026\nScope: notebook workflow, robust_metadata.py, metadata_policy.py, automated tests, and regenerated local outputs.')
    h('1. What changed and why')
    p('The earlier notebook processed six evenly spaced, low-detail video frames, summarized transcripts before synthesis, and required five FAST selections. This could miss brief visual artifacts, discard relevant source wording, produce generic keywords, and encourage marginal subject choices. The new default evidence-first mode improves source coverage and exposes evidence and quality checks for each record. It remains a machine-assisted cataloging workflow, not an autonomous factual authority.')
    table(['Area','Previous behavior','Implemented behavior'],[
       ('Visual evidence','6 low-detail frames','24 frames: coverage plus visual-change sampling; high-detail image input'),
       ('Descriptions','Narrative based on intermediate summaries','5–9 source-linked sentences from exact transcript spans and separate context'),
       ('Keywords','Five strings with count validation','Five distinct phrases with linked source passages and a preference for substantive topics'),
       ('FAST retrieval','Semantic topical retrieval and reranking','Semantic plus lexical topical/geographic retrieval, verified authority IDs, fusion and reranking'),
       ('FAST selection','Exactly five selected candidates','Mandatory collection event plus up to four specific headings; no relevance padding'),
       ('Quality control','Structural checks and selection rationales','Separate text audit, at most one revision, unresolved-issue flags and provenance')])
    h('2. Validation outcome')
    p(f'All six videos completed and were exported with zero processing-error rows. The new test suite contains 19 passing tests. {statuses.get("passed_automated_review",0)} records passed the automated review without remaining flags; {statuses.get("needs_review",0)} records require human review. A completed export is not the same as a factual approval. Remaining flags are retained in Quality_JSON rather than hidden.')
    table(['Interview','Frames','Keywords','FAST total','Review status'],[
       (r['video_filename'].split('-2026')[0],r['sampled_frames'],len(r['keywords']),len(r['fast_subjects']),r['quality']['status']) for r in results])
    p('The baseline files were copied to outputs/baseline_before_robust before regeneration. No human-labeled benchmark was available, so the report claims improved coverage, traceability and validation behavior, not a quantified increase in factual accuracy, subject precision or visual-event recall.')

    page('Visual evidence and source-grounded descriptions')
    h('3. Adaptive frame coverage')
    p('OpenCV first determines duration, frame count and frame rate. Twelve coverage positions are retained at fractions (i + 0.5) / 12. A two-second scan uses 160 × 90 grayscale thumbnails and mean absolute pixel differences to identify visual change; extreme brightness is excluded from the change-score candidates. Additional positions are selected with temporal separation, and fill positions are used when needed, up to ROBUST_FRAME_COUNT=24. Coverage positions remain even for a visually static interview.')
    p('Selected frames are resized within 1280 × 1280 pixels, encoded as JPEG at quality 88, and sent with detail=high. Each frame has a stable ID and timestamp calculated from the actual frame index and frame rate. The model can select only supplied frame IDs; code supplies the final timestamps. This prevents fabricated timestamps but does not prove that an observation is correct or identify the start/end of a continuously occurring event.')
    h('4. Meaningful visual observations')
    p('The visual schema separates attire_and_symbols, artifacts_and_props, and activities_and_emotional_moments. Instructions favor directly observable attire, readable insignia, displayed phones/photos/documents, smiles, gestures and gaze. Routine speaking and studio backgrounds are omitted. Empty categories are valid. The legacy category name includes “emotional,” but the model is explicitly prohibited from diagnosing psychological states, motives or identity from appearance.')
    p('Each observation records high, medium or low ordinal confidence. Low-confidence observations are flagged for review and excluded from evidence supplied to the text-synthesis stage. Confidence is a model judgment, not a calibrated probability. The text auditor does not re-inspect the images, so visual correctness still requires a reviewer to inspect the recording at the cited times.')
    h('5. Transcript preservation and source binding')
    p('The supplied transcript is split into nonoverlapping spans of approximately 900 characters with exact character offsets and source IDs. Joining the spans reconstructs the complete source without truncation or lossy summarization. Recording context is a separate source; the known collection event is another explicitly identified source. A recording date does not become the date of a historical event.')
    p('Synthesis returns 5–9 description sentences and five keyword phrases, each linked to source IDs. The model does not write the final quotations: bind_support() attaches the original source passages directly from those IDs. validate_support() verifies literal correspondence. This design was introduced after the first trial rejected model-copied excerpts that changed or crossed source wording. Programmatic copying solves quotation fidelity, while the separate audit addresses whether a passage actually supports a claim.')
    p('The source-grounding instructions distinguish direct experience, television coverage and inherited family memory. They prohibit guessing redacted names or places, treating an earlier visit as presence during an attack, and inferring historical truth from an unreadable photograph. Transcripts remain the supplied spreadsheet text; fresh audio transcription is not enabled by this mode.')

    page('Keywords, authorized subjects, and review')
    h('6. More useful discovery keywords')
    p('The strict keyword schema requires exactly five supported phrases. Instructions prefer at least three substantive topics rather than five personal or organizational names when the evidence supports that diversity. Code rejects empty or duplicate normalized phrases after case folding and punctuation normalization. Each keyword retains its source passages, and the auditor checks whether it describes meaningful content rather than an incidental mention. The topic-diversity preference is a prompt instruction, not a proven taxonomy or numeric guarantee.')
    h('7. Hybrid FAST candidate retrieval')
    p('The existing FAISS/MMR and cross-encoder path supplies semantic candidates. A new disk-backed SQLite FTS5 index is built from non-deleted local Topical and Geo JSONL records. Lexical queries use extracted themes, locations and organizations and return up to 60 BM25-ranked headings. Candidate identities from both routes are checked against the local authority table; unknown or deleted records and the rejected September 11 “in art” subdivision are not admitted.')
    p('The routes are merged by authority ID using reciprocal-rank fusion, with a contribution of 1 / (60 + rank) from each route. Up to 90 merged records are reranked using cross-encoder/ms-marco-MiniLM-L-6-v2 against the description; at most 30 are passed to final selection. Records preserve authority IDs, facets, retrieval routes, fusion scores and reranker scores. Ranking scores are not confidence probabilities. The semantic index is topical; geographic candidates are supplied by the lexical route.')
    h('8. Evidence-supported selection and collection policy')
    p('The model selects zero to four specific candidate IDs, with source references and centrality rationales. Candidate IDs are constrained by a strict schema, duplicate IDs are rejected, and final labels are taken from the authority records. The collection-wide heading September 11 Terrorist Attacks (2001), fst01112794, is added exactly once as an explicit policy. The preferred FAST label and event-facet identity were verified against the authority resource at https://id.worldcat.org/fast/1112794.')
    p('This intentionally changes the earlier fixed-five rule: a video can have fewer than five total headings if four additional strong subjects are not supported. Forcing the count would defeat the relevance objective. The shared event is distinguished from retrieved/model-selected subjects in the selection details.')
    h('9. Separate text audit and bounded revision')
    p('A separate call using the same metadata model reviews description sentences, keywords and selected FAST headings against the exact sources. It looks for unsupported details, misleading eyewitness claims, incidental keywords and weak subject relevance. When it reports an issue, synthesis receives the feedback and selection is rerun on the revised metadata. Remaining issues, or any low-confidence visual observations, set status=needs_review. A clean response sets passed_automated_review; that label is not human approval or proof of accuracy.')
    for r in results:
        issues=r['quality']['issues']
        if issues:
            p(r['video_filename']+': '+ '; '.join(issues))

    page('Implementation, testing, and operation')
    h('10. Integration and artifacts')
    p('ROBUST_MODE=True is now the notebook default; ROBUST_FRAME_COUNT=24 controls its sampling budget. The prior process_video implementation is retained as the legacy fallback. The notebook continues to use GPT-6 Luna with compatible API parameters and the existing text-embedding-3-large semantic index. robust_metadata.py coordinates the new stages; metadata_policy.py implements the shared event and exclusion rule. No new package installation was required.')
    p('The workbook adds Quality_JSON, Description_Support_JSON, Keyword_Support_JSON and Provenance_JSON. Readable Quality_Review, Evidence_Sources, Description_Evidence, Keyword_Evidence, FAST_Selection and Visual_Evidence worksheets expose the same evidence without requiring JSON parsing. Full JSON additionally contains transcript spans, recording/collection context, frame manifests, individual source links, authority identifiers and retrieval routes. Existing evidence, candidate and uncertainty fields remain available. The CSV and Excel are convenient review formats; full JSON is the richer evidence record.')
    h('11. Caching, cost and failure behavior')
    p('Per-video fingerprints include the implementation SHA-256, model, video path/size/mtime, transcript, context, frame budget and supplied retrieval settings. The lexical authority signature includes local source-file sizes and modification times. Stage requests are separately cached by prompt, schema, payload, model and image fingerprints, allowing identical visual-analysis requests to be reused across implementation revisions. Failed final records are not marked complete.')
    p('A first-pass video uses visual extraction, synthesis, subject selection and audit calls. A full revision adds three text calls, so the normal bound is seven metadata calls per video, excluding SDK transport retries and query-embedding calls. More/high-detail images and auditing can cost more than the baseline. Usage is preserved in provenance; no cost reduction or fixed dollar estimate is claimed. Reruns that reuse cached stages are not newly billed for those cached stages.')
    h('12. Automated and live verification')
    table(['Coverage','Result'],[
      ('Existing contract / export suite','12 tests passed'),
      ('New robustness tests','6 tests passed: source reconstruction, quote rejection, source binding, policy idempotence, authority filtering/fusion, adaptive sampling'),
      ('Notebook evidence export','1 test passed: readable evidence sheets preserve source IDs, original passages and review flags; formula-like source text is escaped'),
      ('Full execution','Six completed video records; zero Errors rows'),
      ('Source integrity','Description, keyword and model-selected FAST passages validated against their referenced sources'),
      ('Limits of verification','No human gold standard, calibrated confidence, independent visual reinspection, or measured recall/precision')])
    p('Run the notebook: .venv/bin/python run_notebook.py. For an interactive session, restart the kernel and run all cells. Run tests: .venv/bin/python -m unittest -v test_notebook_exports.py test_robust_metadata.py test_notebook_contract.py test_pipeline.py. Set ROBUST_MODE=False to return to the legacy path. The new mode is configured for five keywords and a maximum of five total FAST headings.')
    h('13. Recommended next work')
    p('Prioritize human approval of flagged records; a small manually annotated benchmark for artifact detection and subject relevance; optional authorized, time-aligned audio transcription to resolve transcript omissions; verified additional FAST facets and embedding provenance; and targeted second-pass crops or denser sampling around detected prop displays. Evaluate each change against the benchmark before increasing processing cost. A lexical/semantic retrieval system cannot supply missing authority coverage, and no metadata model can reliably reconstruct source redactions without additional evidence.')
    h('Technical references')
    p('OpenAI image-input guidance: https://developers.openai.com/api/docs/guides/images-vision\nOpenAI structured-output guidance: https://developers.openai.com/api/docs/guides/structured-outputs\nFAST event authority: https://id.worldcat.org/fast/1112794\nLocal evidence: notebook source, robust_metadata.py, metadata_policy.py, test suites and the regenerated Excel/JSON.')
    target=ROOT/'outputs/reports/UCF_911_Robust_Metadata_Implementation_Report_2026-11-12.docx'
    target.parent.mkdir(parents=True,exist_ok=True)
    d.core_properties.title='UCF 9/11: Robust Metadata Implementation and Validation'
    d.core_properties.author='Ucfmeta1'
    d.save(target)
    print(target)

if __name__=='__main__':main()

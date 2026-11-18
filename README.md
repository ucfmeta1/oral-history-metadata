# Oral-history metadata pipeline

Creates `outputs/video_metadata.xlsx` from the six MP4 videos and the transcript workbook under `Library-Metadata`.

The current workflow is the notebook: it generates transcripts from video audio, extracts representative visual evidence from eight frames, and exports descriptions, separate entity facets, five keywords, and up to five supported FAST subjects. Start with [Current notebook workflow](#current-notebook-workflow). The standalone `pipeline.py` workflow below is retained as a legacy alternative.

<!-- BEGIN EXCEL VIDEO EXAMPLE -->
## Video example: Ken Lundy — all facets

One generated example from the eight-frame notebook run. All six entity facets and all three visual-evidence categories appear below, including categories with no observations. Values are shown as generated; review flags and transcription uncertainty remain visible.

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Ken (surname spelling uncertain)</li><li>Ken’s wife</li><li>Ken’s friend</li></ul><h4>Locations</h4><ul><li>UCF John C. Hitt Library</li><li>Grand Rapids, Michigan</li><li>New York City</li><li>World Trade Center</li></ul><h4>Organizations</h4><ul><li>UCF</li><li>Knights Tales Project</li><li>Steelcase</li><li>Social Security</li></ul><h4>Dates</h4><ul><li>September 11, 2026 (recording date)</li><li>September 11, 2001 (event date)</li><li>Labor Day 2001 (prior visit)</li></ul><h4>Themes</h4><ul><li>September 11, 2001 attacks</li><li>work and relocation</li><li>World Trade Center visit before the attacks</li><li>family communication</li><li>remembrance and healing</li></ul><h4>Perspective</h4><ul><li>Personal recollection of watching events unfold at Steelcase headquarters in Grand Rapids, combined with memories of a prior World Trade Center visit; the account does not describe being at an attack site during the attacks.</li></ul><h4>Visual evidence</h4><p><strong>Attire and symbols</strong></p><ul><li>15.567 s · V001 · Wearing a black collared top and large translucent, pale-framed glasses with black temples; a small white mark is visible on one temple but is not legible. (confidence: high; review required: False)</li></ul><p><strong>Artifacts and props</strong></p><ul><li>None recorded</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>46.733 s · V002 · Mouth open mid-speech, facing mostly forward with gaze slightly to the side. (confidence: high; review required: False)</li><li>158 s · V006 · Gaze lowered and lips closed; no hand gesture is visible. (confidence: high; review required: False)</li><li>171.367 s · V007 · Mouth open mid-speech, with gaze angled slightly downward to the side. (confidence: high; review required: False)</li></ul>

</td>
<td width="60%" valign="top">

<h3>Ken Lundy</h3><p>187 seconds · 8 sampled frames</p><p>Play/pause and audio controls are available in the GitHub video player.</p>

https://github.com/user-attachments/assets/56694318-b34f-448b-ae63-0d945b35f1cf

<h4>Generated description</h4><p>Ken introduces himself as recording an interview at UCF’s John C. Hitt Library for the Knights Tales Project on September 11, 2026, the 25th anniversary of 9/11. He recalls working for Steelcase, whose headquarters was in Grand Rapids, Michigan, while his territory was New York City. Before the attacks, he and his wife had traveled to the New York City area over Labor Day 2001 to seek employment and housing; he says his first visit to the World Trade Center towers was during that trip. He describes being at Steelcase headquarters in Grand Rapids on September 11, 2001, watching events unfold there, and being unable to reach his wife, who was working for Social Security. He says he later met his wife at home in Grand Rapids and recalls meeting a friend in the World Trade Center shopping area during his earlier visit. He reflects on the people who worked in the World Trade Center, remembers the victims, and expresses hope and prayer for healing. In the supplied video frames, the speaker wears a dark collared top and pale-framed glasses; frames also show him speaking and, at one moment, looking downward.</p><h4>Keywords</h4><ul><li>September 11, 2001 attacks</li><li>Grand Rapids recollections</li><li>World Trade Center visit before the attacks</li><li>family communication during the attacks</li><li>remembrance and healing</li></ul><h4>Selected FAST subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>Victims of terrorism</li></ul><h4>Review status</h4><p>needs_review</p><h4>Review issues</h4><ul><li>The keyword “family communication during the attacks” overstates the coverage: the transcript briefly mentions being unable to reach his wife and later meeting her at home, rather than sustained discussion of family communication.</li><li>The FAST heading “Victims of terrorism” is weakly relevant as a selected heading: victims are mentioned briefly in closing remarks, while the interview primarily recounts the speaker’s own experience. The rationale’s claim that victims are a central topic is unsupported.</li></ul><h4>Uncertainties</h4><ul><li>The transcript identifies the speaker as “Ken Landy,” while the supplied metadata gives the surname as “Lundy”; the surname spelling is unresolved.</li><li>The transcript ends mid-sentence after the speaker says “later on that afternoon,” so the omitted continuation is unknown.</li></ul>

</td>
</tr>
</table>

Source: `outputs/notebook/UCFremembers911_video_metadata.json`, matching the generated Excel workbook. This is a static metadata panel; the video attachment supports playback with audio. [Full example, including evidence support and FAST candidates](examples/ken-lundy-metadata.json). Observations are extracted directly from sampled frames with no post-processing.
<!-- END EXCEL VIDEO EXAMPLE -->

## Legacy script setup and run

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python pipeline.py --check
.venv/bin/python pipeline.py
```

The featured interview is hosted as a GitHub video attachment. The complete collection inputs and authority data are not distributed in this repository. Place one transcript workbook and its MP4 files under `Library-Metadata/`, topical authority JSONL under `Topical/`, and geographic authority JSONL under `Geo/`. Each authority record must contain `id`, `fast` (the authorized heading), and `deleted` fields. The workbook must retain `ResponseId`, `Q1_4` (first name), `Q1_6` (last name), and `Q14_Video_Transcript` columns. Video filenames must include the matching first and last names.

Put the OpenAI API key in `secret.txt` or `secrets.txt`, or set `OPENAI_API_KEY`. Keys are never printed. Running the pipeline sends the interview transcript and sampled frames to OpenAI and incurs API charges. Responses use `store=False`.

Defaults: `gpt-4.1-mini`, 12 evenly spaced low-detail JPEG frames per video, two GPT requests per interview. Override with `--model`, `--frames`, or `--limit 1` for a trial. Existing transcripts avoid transcription charges. Actual token usage is saved in the workbook and JSON; no fixed cost estimate is promised.

## Legacy script workflow

1. Match each spreadsheet row to exactly one video by first/last name, rejecting unmatched or ambiguous inputs.
2. Use transcript, supplied affiliation/occupation/date and sampled video frames to generate a description, entities, perspective, timestamped visual observations and uncertainties.
3. Retrieve the top 30 FAST headings with word/bigram TF-IDF cosine similarity over non-deleted local Topical and Geo JSONL authority records. This is lexical ranking, not semantic embeddings or an OCLC relevance ranking. The existing FAISS/pickle files are not loaded because their embedding model and serialization provenance are undocumented. Local coverage includes only topical and geographic facets; event/name/genre facets may be absent.
4. Ask GPT to select exactly five distinct authority IDs from those candidates with rationales, and generate five distinct discovery keywords. Validate all selections against the candidate enum.
5. Write a metadata sheet, all 30 ranked candidates with authority links and selection rationales, and processing notes with token usage and technical video metadata. Checkpoint each completed interview and description so reruns avoid repeating successful API calls. The workbook updates after every completed interview.

The three DOCX documents informed entity extraction, first-hand versus inherited memory distinctions, visual props, technical metadata, and uncertainty reporting. Their example summaries are not fed to GPT as evidence: some details are redacted in the actual transcripts. The pipeline does not reconstruct redactions. Sampled frames cannot establish complete timelines or guarantee detection of brief props. Audio prosody, transcript alignment, emotional diagnosis, biometrics and voiceprints are outside this implementation. Visual timestamps identify sampled observations, not precise event boundaries. Review generated descriptions and headings before catalog publication.

Output caches contain interview material. Keep `outputs` private. To regenerate an interview, remove its corresponding output cache folder. Changing the model, frame count, video size/mtime or transcript creates a fresh cache. Changes to authority files require deleting existing `result.json` caches. The input files remain untouched.

Official references:
- https://developers.openai.com/api/docs/models/gpt-4.1-mini
- https://developers.openai.com/api/docs/guides/images-vision
- https://www.oclc.org/developer/api/oclc-apis/fast-api/assign-fast.en.html

## Current notebook workflow

`Test_UCFremembers911_video_FAST_metadata.ipynb` is adapted for local execution. It uses GPT-6 Luna with model-compatible API parameters, revised rubric prompts, and the topical FAISS index (`text-embedding-3-large`), MMR retrieval, and cross-encoder reranking. It uses `secret.txt` / `secrets.txt` or `OPENAI_API_KEY` and the `.venv` environment, with no Colab dependency.

```sh
.venv/bin/python -m pip install -r requirements-notebook.txt
.venv/bin/python run_notebook.py
```

Edit configuration cell 5 (`ROOT`, `OUTPUT_DIR`, `TRANSCRIPT_WORKBOOK`, `FAST_DB_DIR`) for a different collection. Audio-generated transcripts are written to `TRANSCRIPT_WORKBOOK` and read back for name-based matching; the original supplied transcript workbook is not required. The notebook exports 30 reranked candidates, five selected headings and five keywords for each video to `outputs/notebook/`, including Excel, CSV, JSON and an executed notebook. On first run the cross-encoder is downloaded; the local FAST index takes several GB of memory. A full run incurs transcription, configured metadata-model, and embedding API charges; cached successful stages are reused. The notebook preserves supplied redactions and puts uncertainty outside the catalog description.

## Robust metadata mode

The notebook now defaults to `ROBUST_MODE = True` and `ROBUST_FRAME_COUNT = 8`. Set `ROBUST_MODE = False` to use the earlier six-frame workflow. Run with:

```sh
.venv/bin/python run_notebook.py
```

The evidence-first mode adds:

- Six evenly spaced coverage frames plus two additional frames chosen from a two-second visual-change scan, up to eight total (67% fewer API images than the previous default). Images are sent at high detail, resized within 1280 × 1280 pixels. This improves coverage but cannot guarantee detection of every short event.
- A compact set of representative observations, matching the reference workbook’s categorized JSON structure in `Visual Evidence JSON`, bound to actual frame IDs, with ordinal confidence labels and low-confidence review flags. No observations are filtered or summarized after extraction. Gestures and expressions are described without diagnosing emotions or identifying faces.
- Exact transcript spans and separate recording/collection context. Description sentences, keywords, and selected FAST subjects carry source IDs and verbatim supporting excerpts. Missing/redacted details are not guessed.
- Semantic retrieval merged with SQLite FTS5 lexical retrieval over non-deleted topical and geographic FAST records. Reciprocal-rank fusion merges the routes; the existing cross-encoder reranks the pool. Unknown/deleted authority IDs and the rejected September 11 “in art” subdivision are excluded.
- The verified collection heading `September 11 Terrorist Attacks (2001)` (`fst01112794`) plus up to four specific candidate headings. Fewer than five total are allowed when the evidence does not support four additional subjects. The universal event is a cataloging policy, not an AI retrieval result.
- A separate text-based evidence audit, with one bounded revision attempt. Remaining issues produce `needs_review`, rather than a claim of validated factual accuracy. This audit is not independent human review or visual reinspection.

The workbook includes `Quality_JSON`, `Description_Support_JSON`, `Keyword_Support_JSON`, and `Provenance_JSON`. Full JSON additionally preserves transcript spans, frame manifests, selection rationales, retrieval routes, model usage and implementation fingerprints. Confidence labels and cross-encoder scores are not calibrated probabilities. API usage increases with more frames and review calls; exact counts are recorded in provenance. Previous baseline files were preserved locally under `outputs/baseline_before_robust/`.

`robust_metadata.py` implements the new workflow. Source quotes are checked literally against exact source spans; those checks validate traceability, not entailment. A reviewer still needs to approve cataloging quality. Audio transcription is enabled in the notebook; audio-derived emotional labels are not generated.

## Audio-generated transcripts and separate entity columns

The notebook now transcribes audio instead of reading the supplied transcript spreadsheet. `TRANSCRIPTION_MODEL = 'gpt-transcribe'` selects the current transcription API model; `whisper-1` can be selected while that model remains available. Audio is extracted locally to mono 16 kHz MP3 and split into ten-minute chunks below the upload limit. Successful chunk transcripts are cached by full video-content SHA-256, model and settings.

The generated source workbook is `outputs/notebook/generated_transcriptions/UCFremembers911_generated_transcriptions.xlsx`. It contains one video per row with `Transcript` plus filename-derived identity/date fields and transcription provenance. The notebook reads this generated Excel file back before metadata generation. Plain-text transcripts and a JSON manifest are retained beside it. The original transcript Excel file is not opened or used as fallback. Speaker affiliation/occupation must now be supported by the audio-generated text; it is not copied from the supplied workbook. Automatic transcription still requires review for names and wording. Chunk starts are approximate chunk positions, not word-aligned timestamps.

The main metadata sheet exports `People`, `Locations`, `Organizations`, `Dates`, `Themes` and `Perspective` as separate columns. List values use `; ` separators without JSON array notation or JSON quoting. Full structured evidence remains in the JSON output and evidence worksheets. Set `DRY_RUN=True` to transcribe and process only the first video; normal mode processes all videos.

Workbook output uses the managed Artifact Tool runtime. `workbook_io.py` discovers it under `~/.cache/codex-runtimes/codex-primary-runtime/dependencies`; set `ARTIFACT_DEPENDENCIES` if the runtime is stored elsewhere. Previous outputs from supplied transcripts are preserved locally under `outputs/before_audio_transcription/`.

### Raw visual evidence

Visual post-processing is disabled. All observations are exported unchanged, including repeated activities and low-confidence observations. The main Visual Evidence column contains the original observations with timestamps, and Visual_Evidence contains one row per observation. There is no processed visual worksheet or processed visual object in the JSON output. Capitalized headers and semicolon-separated entity values are retained.

To refresh the README example after a new notebook run:

```sh
.venv/bin/python examples/build_readme_example.py
```

Run the local checks with `.venv/bin/python -m unittest discover -q`.

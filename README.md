# Oral-history metadata pipeline

Creates `outputs/video_metadata.xlsx` from the six MP4 videos and the transcript workbook under `Library-Metadata`.

## Video example: Ken Lundy

Use the player below to play or pause the interview. GitHub starts the player muted; use the speaker control to enable audio and adjust the volume. This copy preserves the full interview and audio, compressed for browser playback.

https://github.com/user-attachments/assets/56694318-b34f-448b-ae63-0d945b35f1cf

### Generated description

Ken Lundy, a Program Manager at UCF Launch, shares his personal experience during a significant historical event as part of the Knight's Tales Project. Lundy recounts his time working for Steelcase and being in the vicinity of the World Trade Center during a major incident. He describes the communication challenges he faced while trying to contact his spouse amidst the chaos. Lundy reflects on the psychological trauma experienced by many and emphasizes the importance of remembrance and healing for the victims. His narrative provides insight into the immediate aftermath of the event and the broader social impacts. This account contributes to the collective memory of the event, highlighting the personal and professional challenges faced by individuals during crises.

### Generated keywords

Ken Lundy, UCF Launch, Steelcase, World Trade Center, Knight's Tales Project

### Selected FAST subject headings

- Psychic trauma
- Universities and colleges--Professional staff
- Memorials--Psychological aspects
- Healing
- Communication in human services

These are the existing outputs from the supplied notebook workflow, shown unchanged. [View the example metadata as JSON](examples/ken-lundy-metadata.json).

## Proposed discovery interface

A search-and-filter concept for exploring the oral-history collection. The sidebar combines affiliation, visual artifacts, attire, observable gestures, audio events, and thematic subjects; result cards connect each interview to its discovery facets.

```text
+---------------------------------------+--------------------------------------+
| [=] UCF Remembers 9/11       Search transcripts & entities                   |
+---------------------------------------+--------------------------------------+
| [ Sidebar Filters ]                   | Results (Showing 18 items)           |
| v UCF AFFILIATION                     |                                      |
|   [ ] Faculty   [ ] Staff             | +--------------------------------+   |
|   [ ] Alumni    [ ] Student           | | [>] A Pilot's Perspective       |  |
|                                       | | Col. Phillip Jones             |   |
| v VISUAL PROPS & ARTIFACTS            | | Facets:                        |   |
|   [x] Historical Photos               | |   Military Uniform             |   |
|   [ ] Mobile/Digital Screens          | |   Downward Gaze                |   |
|   [ ] Newspaper Clippings             | |   USCENTAF / Shaw AFB           |  |
|                                       | +--------------------------------+   |
| v ATTIRE & SYMBOLS                    |                                      |
|   [x] Military Uniforms               | +--------------------------------+   |
|   [ ] Cultural Garments (Hijab)       | | [>] Witness from Oyster Bar    |   |
|                                       | | Doris Stanley                  |   |
| v BEHAVIORAL & GAZE CUES              | | Facets:                        |   |
|   [x] Downward Gaze / Reflection      | |   Reflective Pause             |   |
|   [ ] Expressive Hand Gestures        | |   Anxiety & Trauma             |   |
|                                       | |   Live TV Broadcasts           |   |
| v PARALINGUISTIC EVENTS               | +--------------------------------+   |
|   [x] Sighs / Trembling Voice         |                                      |
|   [ ] Extended Silent Pauses          |                                      |
|                                       |                                      |
| v THEMATIC ELEMENTS                   |                                      |
|   [x] Military Response & Logistics   |                                      |
|   [x] 2001 Tech & Comm. Barriers      |                                      |
|   [x] Social Aftermath / Backlash     |                                      |
+---------------------------------------+--------------------------------------+
```

This is a static wireframe based on the proposed design. The 18-item count, selected filters, and card facets are illustrative, not verified findings from the six-video run. Audio events and detailed behavioral facets would require additional analysis and review before becoming searchable metadata.

## Setup and run

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python pipeline.py --check
.venv/bin/python pipeline.py
```

The featured interview is hosted as a GitHub video attachment. The complete collection inputs and authority data are not distributed in this repository. Place one transcript workbook and its MP4 files under `Library-Metadata/`, topical authority JSONL under `Topical/`, and geographic authority JSONL under `Geo/`. Each authority record must contain `id`, `fast` (the authorized heading), and `deleted` fields. The workbook must retain `ResponseId`, `Q1_4` (first name), `Q1_6` (last name), and `Q14_Video_Transcript` columns. Video filenames must include the matching first and last names.

Put the OpenAI API key in `secret.txt` or `secrets.txt`, or set `OPENAI_API_KEY`. Keys are never printed. Running the pipeline sends the interview transcript and sampled frames to OpenAI and incurs API charges. Responses use `store=False`.

Defaults: `gpt-4.1-mini`, 12 evenly spaced low-detail JPEG frames per video, two GPT requests per interview. Override with `--model`, `--frames`, or `--limit 1` for a trial. Existing transcripts avoid transcription charges. Actual token usage is saved in the workbook and JSON; no fixed cost estimate is promised.

## Workflow

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

## Supplied notebook workflow

`Test_UCFremembers911_video_FAST_metadata.ipynb` is adapted for local execution. It retains the supplied GPT-4o model, revised rubric prompts, topical FAISS index (`text-embedding-3-large`), MMR retrieval, and cross-encoder reranking. It uses `secret.txt` / `secrets.txt` or `OPENAI_API_KEY` and the `.venv` environment, with no Colab dependency.

```sh
.venv/bin/python -m pip install -r requirements-notebook.txt
.venv/bin/python run_notebook.py
```

Edit configuration cell 5 (`ROOT`, `TRANSCRIPT_WORKBOOK`, `FAST_DB_DIR`) for a different collection. This collection's name-based matching expects `Q1_4`, `Q1_6`, `ResponseId` and `Q14_Video_Transcript`. The notebook exports 30 reranked candidates, five selected headings and five keywords for each video to `outputs/notebook/`, including Excel, CSV, JSON and an executed notebook. On first run the cross-encoder is downloaded; the local FAST index takes several GB of memory. A full run incurs GPT-4o and embedding API charges. The notebook preserves supplied redactions and puts uncertainty outside the catalog description.

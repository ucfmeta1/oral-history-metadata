# Oral-history metadata pipeline

Generates video metadata from the six oral-history interviews. The notebook exports `outputs/notebook/UCFremembers911_video_metadata.xlsx`; the legacy script exports `outputs/video_metadata.xlsx`.

The current workflow is the notebook: it generates transcripts from video audio, extracts representative visual evidence from 15 frames, and exports descriptions, separate entity facets, five keywords, and up to five supported FAST subjects. Start with [Current notebook workflow](#current-notebook-workflow). The standalone `pipeline.py` workflow below is retained as a legacy alternative.

<!-- BEGIN EXCEL VIDEO EXAMPLE -->
## Video examples — all generated results

All 6 interviews from the 15-frame notebook run. Each example includes every entity facet, available visual evidence, the JSON evidence, description, five keywords, FAST subjects, retrieved candidates, and supporting evidence. Every interview has one inline video player with play/pause and audio controls. A fallback link is provided below each player. Results use the original workbook’s speaker names.

- [Danna Arrieta-Ventura](#danna-arrieta-ventura)
- [Chereeka Garner](#chereeka-garner)
- [Phillip Jones](#phillip-jones)
- [Ken Lundy](#ken-lundy)
- [Juan Reyes Sierra](#juan-reyes-sierra)
- [Doris Stanley](#doris-stanley)

### Danna Arrieta-Ventura

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Danna Arrieta-Ventura</li><li>Danna’s mother</li><li>Danna’s great-aunt</li><li>Danna’s former science teacher</li><li>The teacher’s friend</li></ul><h4>Locations</h4><ul><li>Huánuco, Peru</li><li>Lima, Peru</li><li>New York</li><li>United States</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF Remembers 9/11</li><li>World Trade Center</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>Family connections to September 11</li><li>Immigration and transnational family communication</li><li>Fear and uncertainty</li><li>International and cultural effects</li><li>Remembering the aftermath</li></ul><h4>Perspective</h4><ul><li>A family-centered account drawing on inherited memory from the speaker’s great-aunt and a story shared by a former teacher; the speaker does not describe being present at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[31.667 s] the seated person wears a bright red top with a black neckline and large clear-lens glasses; no legible insignia is visible.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[4 s] the person looks downward with lips parted.</li><li>[31.667 s] the person faces forward with mouth open as if speaking.</li><li>[80 s] the person looks down; in later sampled frames they mostly face forward, sometimes with lips parted.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Danna Arrieta-Ventura</h3><p>169 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/ad0a2e53-54f9-4865-97ed-561001bc8423

<p><a href="examples/videos/danna-arrieta-ventura.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Danna Arrieta-Ventura reflects on her family’s connections to the September 11 attacks and their aftermath. She recounts that her mother, an immigrant from Huánuco, Peru, was studying in high school in New York in 2001 and had limited communication with relatives in Peru. Her great-aunt was in Lima when the attacks occurred, listening to the radio and fearing for Danna’s mother while they were unable to communicate. Danna also shares a story from middle school about her former science teacher’s friend, who worked near the World Trade Center and was surrounded and hidden by coworkers and friends while walking in New York in the weeks afterward. She describes the attacks’ cultural impact and fear as extending beyond the United States, and emphasizes the importance of remembering those effects internationally. Her account centers on family and community memories rather than a claim of personal presence at an attack site.</p><h4>Keywords</h4><ul><li>September 11 family memories</li><li>Peru and transnational family communication</li><li>Fear and uncertainty after the attacks</li><li>Cultural impact in New York</li><li>International remembrance of September 11</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>Women immigrants--Family relationships</li></ul>

</td>
</tr>
</table>

<details><summary>Visual evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "frame_id": "V003",
      "category": "attire_and_symbols",
      "observation": "the seated person wears a bright red top with a black neckline and large clear-lens glasses; no legible insignia is visible.",
      "timestamp_seconds": 31.667
    },
    {
      "frame_id": "V001",
      "category": "activities_and_emotional_moments",
      "observation": "the person looks downward with lips parted.",
      "timestamp_seconds": 4.0
    },
    {
      "frame_id": "V003",
      "category": "activities_and_emotional_moments",
      "observation": "the person faces forward with mouth open as if speaking.",
      "timestamp_seconds": 31.667
    },
    {
      "frame_id": "V007",
      "category": "activities_and_emotional_moments",
      "observation": "the person looks down; in later sampled frames they mostly face forward, sometimes with lips parted.",
      "timestamp_seconds": 80.0
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>2. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>3. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>4. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>5. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>6. Monumento a Túpac Amaru II (Yanaoca, Peru) (fst01025886)</li><li>7. September (fst01112793)</li><li>8. Peru--Puerto Inca (Huánuco) (fst01314272)</li><li>9. Peru--Santa Marta (Huánuco) (fst01319201)</li><li>10. Peru--Huánuco (fst01223929)</li><li>11. Women immigrants--Family relationships (fst01177771)</li><li>12. Peru--Lima--Quinta Heeren (fst01715160)</li><li>13. Peru--Santa María (Huánuco) (fst01322373)</li><li>14. Immigrant families (fst01746411)</li><li>15. Peru--Huánuco (Department) (fst01715148)</li><li>16. Peru--Huánuco (Diocese) (fst01336116)</li><li>17. Connections (Mathematics) (fst00875339)</li><li>18. Migrant labor--Family relationships (fst01020719)</li><li>19. Emigration and immigration--International cooperation (fst00908706)</li><li>20. Peru--Lima--El Agustino (fst01715155)</li><li>21. Peru--San Bartolo (Lima) (fst01871940)</li><li>22. Peru--Huánuco Pampa (fst01235122)</li><li>23. Peru--Barranca (Lima) (fst01314882)</li><li>24. Peru--Huánuco Pampa Site (fst01245200)</li><li>25. Peru--Lima--Huáscar (fst01715156)</li><li>26. Emigrant remittances--Psychological aspects (fst00908689)</li><li>27. Peru--Chancay (Lima) (fst01320876)</li><li>28. Cultural policy--Foreign influences (fst01352666)</li><li>29. United States--United States Highway 11 (fst01891439)</li><li>30. Civics, Peruvian (fst00862429)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/danna-arrieta-ventura.json).

### Chereeka Garner

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Chereeka Garner</li></ul><h4>Locations</h4><ul><li>UCF John C. Hitt Library</li><li>University High School, Orlando, Florida</li><li>World Trade Center</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF</li><li>Night Tales Project</li><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11 attacks</li><li>high school memories</li><li>television news coverage</li><li>school dismissal and family response</li><li>personal recollection</li></ul><h4>Perspective</h4><ul><li>First-person recollection of the attacks’ news and effects at school; Garner describes television coverage and does not claim to have been at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[6 s] The seated speaker wears a white outer layer over a dark navy top with a broad folded collar; no legible insignia is visible.</li></ul><p><strong>Artifacts and props</strong></p><ul><li>6 s · V001 · A large gray microphone on an adjustable arm extends into the foreground from the left; a second microphone is visible at the upper right. No handheld phone, photograph, or document is visible.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[40 s] The speaker faces forward with mouth open mid-speech and eyes directed toward the camera.</li><li>[102.9 s] The speaker briefly narrows her eyes and tightens her mouth while continuing to address the camera.</li><li>[185.233 s] While speaking, the speaker glances upward and to her left rather than directly toward the camera.</li><li>[226.4 s] The speaker looks forward with widened eyes and rounded, open lips mid-speech.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Chereeka Garner</h3><p>329 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/1fdbbf3b-c853-4382-88d9-0274cb13f681

<p><a href="examples/videos/chereeka-garner.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Chereeka Garner recounts her experience as a high school senior on September 11, 2001, in an interview recorded at UCF’s John C. Hitt Library for the Night Tales Project. She was attending University High School in Orlando and arrived early to join her senior class for a panoramic yearbook photograph. After helping clean up, she waited in the courtyard and later crossed to another campus, where she found students watching television and learned that a plane had hit the World Trade Center. Garner recalls watching repeated news coverage, feeling confused by the quiet and by the sparse presence of people around her, and calling her father to ask what was happening. She describes seeing a long line of parents signing students out of school and eventually remaining at school until the end of the day. She says she understood the magnitude of the attacks more fully after she went home and found that her father had left work early.</p><h4>Keywords</h4><ul><li>September 11, 2001 in a high school</li><li>television coverage of the attacks</li><li>school dismissal and parents signing students out</li><li>family response to breaking news</li><li>senior class panoramic photograph</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>September 11 Terrorist Attacks, 2001, on television</li></ul>

</td>
</tr>
</table>

<details><summary>Visual evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "frame_id": "V001",
      "category": "attire_and_symbols",
      "observation": "The seated speaker wears a white outer layer over a dark navy top with a broad folded collar; no legible insignia is visible.",
      "timestamp_seconds": 6.0
    },
    {
      "frame_id": "V001",
      "category": "artifacts_and_props",
      "observation": "A large gray microphone on an adjustable arm extends into the foreground from the left; a second microphone is visible at the upper right. No handheld phone, photograph, or document is visible.",
      "timestamp_seconds": 6.0
    },
    {
      "frame_id": "V003",
      "category": "activities_and_emotional_moments",
      "observation": "The speaker faces forward with mouth open mid-speech and eyes directed toward the camera.",
      "timestamp_seconds": 40.0
    },
    {
      "frame_id": "V006",
      "category": "activities_and_emotional_moments",
      "observation": "The speaker briefly narrows her eyes and tightens her mouth while continuing to address the camera.",
      "timestamp_seconds": 102.9
    },
    {
      "frame_id": "V010",
      "category": "activities_and_emotional_moments",
      "observation": "While speaking, the speaker glances upward and to her left rather than directly toward the camera.",
      "timestamp_seconds": 185.233
    },
    {
      "frame_id": "V011",
      "category": "activities_and_emotional_moments",
      "observation": "The speaker looks forward with widened eyes and rounded, open lips mid-speech.",
      "timestamp_seconds": 226.4
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>2. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>3. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>4. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>5. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>6. Florida--Orlando--Holy Land Experience (fst01905680)</li><li>7. September (fst01112793)</li><li>8. Library orientation for high school students (fst00997853)</li><li>9. High schools--Yearbooks (fst00956345)</li><li>10. Library orientation for junior high school students (fst00997856)</li><li>11. Library orientation for high school students--Evaluation (fst00997854)</li><li>12. Horror tales--Library resources (fst00960394)</li><li>13. Local Library Cooperation Project (fst01001196)</li><li>14. High school students--Family relationships (fst00956194)</li><li>15. Florida--Orlando Metropolitan Area (fst01343966)</li><li>16. Library publications (fst00997882)</li><li>17. School employees--Dismissal of (fst01107347)</li><li>18. Recollection (Psychology) (fst01091460)</li><li>19. Journalism, High school (fst00984138)</li><li>20. High schools--U.S. states (fst00956343)</li><li>21. Florida--Orlando Suburban Area (fst01343968)</li><li>22. South Bay High (Imaginary organization) (fst01743481)</li><li>23. Anecdotes (fst00808608)</li><li>24. Recollection (Theology) (fst01091465)</li><li>25. Public universities and colleges--Libraries (fst01083117)</li><li>26. Florida--Tallahassee--University Park (fst01329164)</li><li>27. World politics--Library resources (fst01181393)</li><li>28. Neighborhood Information Center Project (fst01035615)</li><li>29. Television in university extension (fst01146945)</li><li>30. Autobiographical memory (fst00822589)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/chereeka-garner.json).

### Phillip Jones

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Phillip Jones</li><li>Dwayne Williams</li></ul><h4>Locations</h4><ul><li>Shaw Air Force Base</li><li>Egypt</li><li>United Arab Emirates</li><li>Sumter, South Carolina</li><li>the Pentagon</li><li>the Middle East</li><li>Afghanistan</li><li>Iraq</li></ul><h4>Organizations/ Initiatives</h4><ul><li>U.S. CENTAF</li><li>U.S. Air Force</li><li>U.S. Army</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>2026-09-11</li></ul><h4>Themes</h4><ul><li>military planning and response</li><li>deployment logistics</li><li>support for personnel overseas</li><li>television coverage of the attacks</li><li>remembrance and loss</li></ul><h4>Perspective</h4><ul><li>First-person retrospective oral history focused on Jones’s work and response at Shaw Air Force Base; he recounts seeing the attacks on television and does not describe being at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[19.033 s] the man wears a royal-blue collared shirt and a dark navy cap. The cap has yellow “USCENTAF” lettering above a white airplane graphic and smaller white text reading “COLONEL PJ JONES” and “1974–2000.”</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[19.033 s] he faces forward with his gaze toward the camera and lips slightly parted.</li><li>[32 s] his mouth is open, showing his teeth, while his gaze is directed slightly downward.</li><li>[152 s] his head is lowered and his eyes are closed; his mouth is open.</li><li>[300 s] he looks downward with his mouth closed.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Phillip Jones</h3><p>305 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/df0aa204-9ee7-4d20-8c0a-789cf0a7246d

<p><a href="examples/videos/phillip-jones.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Phillip Jones, a retired Air Force colonel, recalls serving as deputy A5 at U.S. CENTAF at Shaw Air Force Base on September 11, 2001. While watching television at work, he saw the second airplane hit and recognized that the attack was not an accident; he describes his response from Shaw, not being at an attack site. He sent office staff and conference participants home, then helped cancel programs, plan deployments to the Middle East, and arrange support and transportation for personnel in Egypt. Jones recounts that UAE visitors in Sumter, South Carolina, were confined to their hotel rooms after being roughed up, and that military transport was arranged to return them and the Egyptians home. He says he worked without a day off for about 90 days, later contributing to planning for the wars in Afghanistan and Iraq. Jones also remembers his friend Dwayne Williams, an Army major who perished, and reflects on the loss for Williams’s family and colleagues.</p><h4>Keywords</h4><ul><li>military response and deployment planning</li><li>transportation and support for personnel overseas</li><li>U.S. CENTAF at Shaw Air Force Base</li><li>television coverage of September 11</li><li>remembrance of Dwayne Williams</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>South Carolina--Shaw Air Force Base</li></ul>

</td>
</tr>
</table>

<details><summary>Visual evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "frame_id": "V001",
      "category": "attire_and_symbols",
      "observation": "the man wears a royal-blue collared shirt and a dark navy cap. The cap has yellow “USCENTAF” lettering above a white airplane graphic and smaller white text reading “COLONEL PJ JONES” and “1974–2000.”",
      "timestamp_seconds": 19.033
    },
    {
      "frame_id": "V001",
      "category": "activities_and_emotional_moments",
      "observation": "he faces forward with his gaze toward the camera and lips slightly parted.",
      "timestamp_seconds": 19.033
    },
    {
      "frame_id": "V002",
      "category": "activities_and_emotional_moments",
      "observation": "his mouth is open, showing his teeth, while his gaze is directed slightly downward.",
      "timestamp_seconds": 32.0
    },
    {
      "frame_id": "V008",
      "category": "activities_and_emotional_moments",
      "observation": "his head is lowered and his eyes are closed; his mouth is open.",
      "timestamp_seconds": 152.0
    },
    {
      "frame_id": "V015",
      "category": "activities_and_emotional_moments",
      "observation": "he looks downward with his mouth closed.",
      "timestamp_seconds": 300.0
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. South Carolina--Shaw Air Force Base (fst01219335)</li><li>2. Shaw alphabet (fst01115371)</li><li>3. Florida--Eglin Air Force Base (fst01214481)</li><li>4. South Carolina--Myrtle Beach Air Force Base (fst01238171)</li><li>5. North Carolina--Pope Air Force Base (fst01277322)</li><li>6. South Africa--Swartkop Air Force Base (fst01877526)</li><li>7. Egypt (Maine : Imaginary place) (fst00903913)</li><li>8. North Carolina--Seymour Johnson Air Force Base (fst01927912)</li><li>9. Texas--Dyess Air Force Base (fst01214180)</li><li>10. Alaska--Ladd Air Force Base (fst01214544)</li><li>11. Georgia--Moody Air Force Base (fst01204246)</li><li>12. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>13. Georgia--Robins Air Force Base (fst01204249)</li><li>14. Texas--Randolph Air Force Base (fst01213140)</li><li>15. Florida--Tyndall Air Force Base (fst01206061)</li><li>16. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>17. South Carolina--Sumter Junction (fst01263183)</li><li>18. South Dakota--Ellsworth Air Force Base (fst01271967)</li><li>19. California--Vandenberg Air Force Base (fst01210320)</li><li>20. Virginia--Langley Air Force Base (fst01212030)</li><li>21. Egypt in the Bible (fst00903914)</li><li>22. United Arab Emirates--Saqr Harbor (fst01263238)</li><li>23. Texas--Brooks Air Force Base (fst01213141)</li><li>24. Tennessee--Arnold Air Force Base (fst01214614)</li><li>25. United Arab Emirates--ʻAjmān (fst01209210)</li><li>26. California--Norton Air Force Base (fst01212905)</li><li>27. Egyptology (fst00904000)</li><li>28. Texas--Kelly Air Force Base (fst01212914)</li><li>29. Nevada--Nellis Air Force Base (fst01203478)</li><li>30. Alabama--Maxwell Air Force Base (fst01216242)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/phillip-jones.json).

### Ken Lundy

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Ken Lundy</li></ul><h4>Locations</h4><ul><li>UCF John C. Hitt Library</li><li>New York City</li><li>Grand Rapids, Michigan</li><li>World Trade Center</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF</li><li>Knights Tales Project</li><li>Steelcase</li><li>Social Security</li><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>Labor Day 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11 attacks</li><li>work and relocation</li><li>witnessing events from afar</li><li>World Trade Center visit</li><li>remembrance and healing</li></ul><h4>Perspective</h4><ul><li>Personal recollection of watching the events unfold from Steelcase headquarters in Grand Rapids, alongside memories of a prior visit to the World Trade Center; the account does not place Lundy at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[26 s] the man wears a black collared shirt and large, translucent light-colored rectangular glasses with dark temples; no clear insignia is visible.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[74 s] he faces forward with his mouth open and teeth visible, as if speaking; his gaze is slightly lowered.</li><li>[128.533 s] he smiles broadly with teeth visible, looking slightly downward through his glasses.</li><li>[4 s] he turns his face and gaze to the right of the frame, with his mouth slightly open.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Ken Lundy</h3><p>187 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/56694318-b34f-448b-ae63-0d945b35f1cf

<p><a href="examples/videos/ken-lundy.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Ken Lundy recorded this interview at UCF’s John C. Hitt Library for the Knights Tales Project on September 11, 2026, the 25th anniversary of the September 11 attacks. At the time of the attacks, Lundy worked for Steelcase, whose headquarters was in Grand Rapids, Michigan, and his territory was New York City. He and his wife had recently traveled to the New York City area to find work and a place to stay, then returned to Grand Rapids before September 11. Lundy says he watched events unfold at Steelcase headquarters and could not reach his wife, who was working for Social Security; they met at home later that afternoon. He first visited the World Trade Center towers on Labor Day 2001, met a friend in the shopping area, and recalls seeing people who worked in the building. Lundy remembers the victims and expresses hope and prayer for healing. The interview is part of the UCF Remembers 9/11 collection.</p><h4>Keywords</h4><ul><li>September 11, 2001 attacks</li><li>World Trade Center visit</li><li>Steelcase headquarters in Grand Rapids</li><li>New York City employment and relocation</li><li>remembrance and healing</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>New York (State)--New York--World Trade Center Site</li></ul>

</td>
</tr>
</table>

<details><summary>Visual evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "frame_id": "V003",
      "category": "attire_and_symbols",
      "observation": "the man wears a black collared shirt and large, translucent light-colored rectangular glasses with dark temples; no clear insignia is visible.",
      "timestamp_seconds": 26.0
    },
    {
      "frame_id": "V006",
      "category": "activities_and_emotional_moments",
      "observation": "he faces forward with his mouth open and teeth visible, as if speaking; his gaze is slightly lowered.",
      "timestamp_seconds": 74.0
    },
    {
      "frame_id": "V011",
      "category": "activities_and_emotional_moments",
      "observation": "he smiles broadly with teeth visible, looking slightly downward through his glasses.",
      "timestamp_seconds": 128.533
    },
    {
      "frame_id": "V001",
      "category": "activities_and_emotional_moments",
      "observation": "he turns his face and gaze to the right of the frame, with his mouth slightly open.",
      "timestamp_seconds": 4.0
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. Horror tales--Library resources (fst00960394)</li><li>2. Local Library Cooperation Project (fst01001196)</li><li>3. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>4. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>5. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>6. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>7. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>8. Tales From the Floating Vagabond (Game) (fst01142267)</li><li>9. Virginia--John W. Warner Rapids (fst01878859)</li><li>10. Exhibition Hall (United States Capitol Visitor Center, Washington, D.C.) (fst01769267)</li><li>11. Washington (D.C.)--John F. Kennedy Center Plaza (fst01327677)</li><li>12. World War II Memorial (Washington, D.C.) (fst01180739)</li><li>13. Trylon and Perisphere (New York, N.Y.) (fst01911272)</li><li>14. Community college libraries (fst00870710)</li><li>15. Neighborhood Information Center Project (fst01035615)</li><li>16. Buildings--Library resources (fst00841085)</li><li>17. World politics--Library resources (fst01181393)</li><li>18. Lumbermen&#x27;s Monument (Mich.) (fst01746769)</li><li>19. Imagine Peace Tower (Viðey, Iceland) (fst01764135)</li><li>20. New York (State)--New York--World Trade Center Site (fst01328038)</li><li>21. September (fst01112793)</li><li>22. Tales--Social aspects (fst01142257)</li><li>23. Michigan--Grand Rapids Metropolitan Area (fst01347388)</li><li>24. New York (State)--Guilderland Center (fst01229406)</li><li>25. New York (State)--Ontario Center (fst01268210)</li><li>26. New York (State)--Center Moriches (fst01257864)</li><li>27. North Dakota--Grand Rapids (fst01280194)</li><li>28. New York (State)--New York--Grand Concourse (fst01922086)</li><li>29. Michigan--East Grand Rapids (fst01232068)</li><li>30. Michigan--Grand Rapids Suburban Area (fst01347390)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/ken-lundy.json).

### Juan Reyes Sierra

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Juan Reyes Sierra</li><li>Juan&#x27;s father</li><li>George W. Bush</li></ul><h4>Locations</h4><ul><li>Sarasota, Florida</li><li>Longboat Key, Florida</li><li>Colony Beach and Resort</li><li>Booker Elementary School</li><li>Sarasota Airport</li></ul><h4>Organizations/ Initiatives</h4><ul><li>University of Central Florida (UCF)</li><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>2026-09-11</li></ul><h4>Themes</h4><ul><li>September 11 attacks</li><li>family memory</li><li>presidential visit</li><li>hotel management and event logistics</li><li>Sarasota Airport closure</li><li>fighter jets</li></ul><h4>Perspective</h4><ul><li>A UCF student&#x27;s account of his father&#x27;s experience, recalled and shared as family memory; the speaker was not born at the time and does not describe personal presence at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[22 s] the seated person wears a dark jacket over a black top, with a light gray strap visible over one shoulder; no legible insignia is visible.</li></ul><p><strong>Artifacts and props</strong></p><ul><li>110 s · V013 · At 110.0 seconds, a small black microphone with a fuzzy windscreen is visible below the person&#x27;s chin.</li><li>90 s · V010 · At 90.0 seconds, a hand holds a black smartphone close to the camera. Its screen shows a photograph of two people wearing white shirts and ties, one dark and one red; the pictured people are not identified.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[16 s] the person faces forward with mouth open and gaze angled slightly upward.</li><li>[46.867 s] the person lowers their head and looks down.</li><li>[90 s] the person raises the phone toward the camera while looking forward.</li><li>[96 s] the person looks upward with eyes wide and mouth slightly open.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Juan Reyes Sierra</h3><p>150 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/555a06d6-3591-4e93-af75-2a084bedf1f6

<p><a href="examples/videos/juan-reyes-sierra.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Juan Reyes Sierra, a UCF senior from Sarasota, Florida, shares his father’s account of September 11, 2001; Juan says he was not yet born when the attacks happened. His father was a manager at the Colony Beach and Resort in Longboat Key and helped coordinate logistics during President George W. Bush’s stay there on the morning of September 11. Juan says his father recalled preparations for a brunch menu and had a photograph taken with the president. According to the account Juan relays, his father learned of the unfolding events when Sarasota Airport closed and fighter jets were present; the family account describes fears that the president might be targeted. Juan presents the story as inherited family memory rather than a personal experience of the attacks, and says he feels proud to share his father’s connection to the president.</p><h4>Keywords</h4><ul><li>September 11 family memory</li><li>George W. Bush&#x27;s Sarasota visit</li><li>Colony Beach and Resort management</li><li>Sarasota Airport closure and fighter jets</li><li>intergenerational remembrance</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>Florida--Sarasota</li></ul>

</td>
</tr>
</table>

<details><summary>Visual evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "frame_id": "V004",
      "category": "attire_and_symbols",
      "observation": "the seated person wears a dark jacket over a black top, with a light gray strap visible over one shoulder; no legible insignia is visible.",
      "timestamp_seconds": 22.0
    },
    {
      "frame_id": "V013",
      "category": "artifacts_and_props",
      "observation": "At 110.0 seconds, a small black microphone with a fuzzy windscreen is visible below the person's chin.",
      "timestamp_seconds": 110.0
    },
    {
      "frame_id": "V010",
      "category": "artifacts_and_props",
      "observation": "At 90.0 seconds, a hand holds a black smartphone close to the camera. Its screen shows a photograph of two people wearing white shirts and ties, one dark and one red; the pictured people are not identified.",
      "timestamp_seconds": 90.0
    },
    {
      "frame_id": "V003",
      "category": "activities_and_emotional_moments",
      "observation": "the person faces forward with mouth open and gaze angled slightly upward.",
      "timestamp_seconds": 16.0
    },
    {
      "frame_id": "V006",
      "category": "activities_and_emotional_moments",
      "observation": "the person lowers their head and looks down.",
      "timestamp_seconds": 46.867
    },
    {
      "frame_id": "V010",
      "category": "activities_and_emotional_moments",
      "observation": "the person raises the phone toward the camera while looking forward.",
      "timestamp_seconds": 90.0
    },
    {
      "frame_id": "V011",
      "category": "activities_and_emotional_moments",
      "observation": "the person looks upward with eyes wide and mouth slightly open.",
      "timestamp_seconds": 96.0
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. Florida--Sarasota (fst01207248)</li><li>2. Florida--Sarasota Metropolitan Area (fst01343986)</li><li>3. Florida--Sarasota Region (fst01343987)</li><li>4. Florida--Sarasota County (fst01214943)</li><li>5. Florida--Sarasota Bay Region (fst01343985)</li><li>6. Florida--Sarasota Bay Watershed (fst01877821)</li><li>7. Florida--Manasota Key (fst01308766)</li><li>8. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>9. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>10. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>11. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>12. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>13. Florida--Florida State University Reservation (fst01882094)</li><li>14. Florida--Lido Key (fst01241082)</li><li>15. Florida--Saint Armands Key (fst01242110)</li><li>16. Florida--Key Biscayne (fst01210669)</li><li>17. Florida--Siesta Key (fst01215775)</li><li>18. Florida--Jupiter Inlet Colony (fst01232504)</li><li>19. Florida--Perdido Key (fst01307560)</li><li>20. Florida language (fst00927686)</li><li>21. Florida--Pensacola Beach (fst01205000)</li><li>22. Florida--Egmont Key (fst01889144)</li><li>23. Florida--Key Largo (fst01219956)</li><li>24. Florida--Key West (fst01207829)</li><li>25. Florida--Miami Beach (fst01204159)</li><li>26. Florida--Daytona Beach (fst01202733)</li><li>27. Florida--Apollo Beach (fst01210771)</li><li>28. Florida--Cocoa Beach (fst01212556)</li><li>29. Florida--Key West Region (fst01343952)</li><li>30. Florida--Conch Key (fst01886640)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/juan-reyes-sierra.json).

### Doris Stanley

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Doris Stanley</li></ul><h4>Locations</h4><ul><li>New York</li><li>Pennsylvania</li><li>the Pentagon</li><li>UCF</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF</li><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11 attacks</li><li>television coverage</li><li>restaurant work</li><li>emotional aftermath</li><li>anxiety and panic attacks</li><li>counseling</li><li>memorial visit and healing</li></ul><h4>Perspective</h4><ul><li>Personal recollection of witnessing television coverage while working at a restaurant, with reflections on its later effects and a subsequent memorial visit; not an account of being physically present at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[18.033 s] She wears a dark, collared, button-front shirt; no legible insignia is visible.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[2 s] She holds a hand over her mouth and looks forward.</li><li>[126.233 s] She lowers her head and looks down; this downward gaze recurs in later frames.</li><li>[90.167 s] She faces forward with a visible smile.</li><li>[198.367 s] She turns her gaze to her left and slightly downward.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Doris Stanley</h3><p>289 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/f9be7b37-b4aa-41ad-bb88-7bf68a76879c

<p><a href="examples/videos/doris-stanley.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Doris Stanley recounts being 21 and working at an oyster-bar restaurant when television coverage of the September 11 attacks interrupted preparations for lunch. She describes watching repeated footage of the attacks in New York, the Pentagon, and Pennsylvania, including the collapse of a World Trade Center building. Stanley recalls feeling shocked and frightened, and says the footage continued for hours before she asked her boss whether the televisions could be turned off. She connects the experience to later anxiety and panic attacks, fear of heights and bridges, and counseling at UCF, where she says she explored its services and unpacked the experience. Stanley says a later visit to the New York memorial during a conference was healing, and reflects that she felt the loss despite not believing she had personally lost anyone. Recorded for the UCF Remembers 9/11 collection on September 11, 2026, this account centers on television-viewing and its lasting personal effects, rather than physical presence at an attack site.</p><h4>Keywords</h4><ul><li>September 11 television coverage</li><li>World Trade Center collapse</li><li>long-term anxiety and panic attacks</li><li>UCF counseling services</li><li>New York memorial visit</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>September 11 Terrorist Attacks, 2001, on television</li><li>Anxiety</li><li>Counseling--Practice</li></ul>

</td>
</tr>
</table>

<details><summary>Visual evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "frame_id": "V002",
      "category": "attire_and_symbols",
      "observation": "She wears a dark, collared, button-front shirt; no legible insignia is visible.",
      "timestamp_seconds": 18.033
    },
    {
      "frame_id": "V001",
      "category": "activities_and_emotional_moments",
      "observation": "She holds a hand over her mouth and looks forward.",
      "timestamp_seconds": 2.0
    },
    {
      "frame_id": "V008",
      "category": "activities_and_emotional_moments",
      "observation": "She lowers her head and looks down; this downward gaze recurs in later frames.",
      "timestamp_seconds": 126.233
    },
    {
      "frame_id": "V005",
      "category": "activities_and_emotional_moments",
      "observation": "She faces forward with a visible smile.",
      "timestamp_seconds": 90.167
    },
    {
      "frame_id": "V011",
      "category": "activities_and_emotional_moments",
      "observation": "She turns her gaze to her left and slightly downward.",
      "timestamp_seconds": 198.367
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>2. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>3. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>4. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>5. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>6. Restaurant management--Periodicals (fst01095901)</li><li>7. Rehabilitation counseling--Field work (fst01093359)</li><li>8. Restaurants--Food service (fst01095933)</li><li>9. Counseling--Practice (fst00881230)</li><li>10. Restaurant management (fst01095899)</li><li>11. Restaurants--Personnel management (fst01095946)</li><li>12. Short-term counseling (fst01117479)</li><li>13. Hotel restaurants (fst01763303)</li><li>14. Pentagon (fst01057151)</li><li>15. Pentagon Memorial (Va.) (fst01200546)</li><li>16. Counseling--Psychological aspects (fst00881231)</li><li>17. Restaurant management--Prices (fst01095902)</li><li>18. Counseling (fst00881212)</li><li>19. September (fst01112793)</li><li>20. Educational counseling (fst00903395)</li><li>21. Family counseling (fst00920300)</li><li>22. Television in counseling (fst01146878)</li><li>23. Health counseling (fst00952875)</li><li>24. Pentagon in architecture (fst01057152)</li><li>25. Pentagon in art (fst01057153)</li><li>26. Counseling psychology (fst01740078)</li><li>27. Anxiety on television (fst02021893)</li><li>28. Mental health counseling (fst01016395)</li><li>29. Pennsylvania--York (fst01202834)</li><li>30. Anxiety (fst00810950)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/doris-stanley.json).

Source: notebook metadata records. Visual observations are retained without post-processing.
<!-- END EXCEL VIDEO EXAMPLE -->

## Legacy script setup and run

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python pipeline.py --check
.venv/bin/python pipeline.py
```

The featured interview is hosted as a GitHub video attachment. Compressed viewing copies for all six interviews are included under `examples/videos/`; the original collection inputs and authority data are not distributed in this repository. Place one transcript workbook and its MP4 files under `Library-Metadata/`, topical authority JSONL under `Topical/`, and geographic authority JSONL under `Geo/`. Each authority record must contain `id`, `fast` (the authorized heading), and `deleted` fields. The workbook must retain `ResponseId`, `Q1_4` (first name), `Q1_6` (last name), and `Q14_Video_Transcript` columns. Video filenames must include the matching first and last names.

Put the OpenAI API key in `secret.txt` or `secrets.txt`, or set `OPENAI_API_KEY`. Keys are never printed. Running the pipeline sends the interview transcript and sampled frames to OpenAI and incurs API charges. Responses use `store=False`.

Defaults: `gpt-4.1-mini`, 12 evenly spaced low-detail JPEG frames per video, two GPT requests per interview. Override with `--model`, `--frames`, or `--limit 1` for a trial. Existing transcripts avoid transcription charges. Actual token usage is saved in the workbook and JSON; no fixed cost estimate is promised.

## Legacy script workflow

1. Match each spreadsheet row to exactly one video by first/last name, rejecting unmatched or ambiguous inputs.
2. Use transcript, supplied affiliation/occupation/date and sampled video frames to generate a description, entities, perspective, timestamped visual observations.
3. Retrieve the top 30 FAST headings with word/bigram TF-IDF cosine similarity over non-deleted local Topical and Geo JSONL authority records. This is lexical ranking, not semantic embeddings or an OCLC relevance ranking. The existing FAISS/pickle files are not loaded because their embedding model and serialization provenance are undocumented. Local coverage includes only topical and geographic facets; event/name/genre facets may be absent.
4. Ask GPT to select exactly five distinct authority IDs from those candidates with rationales, and generate five distinct discovery keywords. Validate all selections against the candidate enum.
5. Write a metadata sheet, all 30 ranked candidates with authority links and selection rationales, and processing notes with token usage and technical video metadata. Checkpoint each completed interview and description so reruns avoid repeating successful API calls. The workbook updates after every completed interview.

The three DOCX documents informed entity extraction, first-hand versus inherited memory distinctions, visual props, technical metadata. Their example summaries are not fed to GPT as evidence: some details are redacted in the actual transcripts. The pipeline does not reconstruct redactions. Sampled frames cannot establish complete timelines or guarantee detection of brief props. Audio prosody, transcript alignment, emotional diagnosis, biometrics and voiceprints are outside this implementation. Visual timestamps identify sampled observations, not precise event boundaries.

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

Edit configuration cell 5 (`ROOT`, `OUTPUT_DIR`, `TRANSCRIPT_WORKBOOK`, `FAST_DB_DIR`) for a different collection. Audio-generated transcripts are written to `TRANSCRIPT_WORKBOOK` and read back for name-based matching; `NAME_AUTHORITY_WORKBOOK` identifies the original workbook used only for speaker-name fields (`Q1_4`–`Q1_6`). The notebook exports 30 reranked candidates, five selected headings and five keywords for each video to `outputs/notebook/`, including Excel, CSV, JSON and an executed notebook. On first run the cross-encoder is downloaded; the local FAST index takes several GB of memory. A full run incurs transcription, configured metadata-model, and embedding API charges; cached successful stages are reused. The notebook preserves supplied redactions.

## Robust metadata mode

The notebook now defaults to `ROBUST_MODE = True` and `ROBUST_FRAME_COUNT = 15`. Set `ROBUST_MODE = False` to use the earlier six-frame workflow. Run with:

```sh
.venv/bin/python run_notebook.py
```

The evidence-first mode adds:

- Eight evenly spaced coverage frames plus seven additional frames chosen from a two-second visual-change scan, up to 15 total. Images are sent at high detail, resized within 1280 × 1280 pixels. This improves coverage but cannot guarantee detection of every short event.
- A compact set of representative observations, matching the reference workbook’s categorized JSON structure in `Visual Evidence JSON` (indented JSON, validated against the reference field names and types), bound to actual frame IDs. No observations are filtered or summarized after extraction. Gestures and expressions are described without diagnosing emotions or identifying faces.
- Exact transcript spans and separate recording/collection context. Description sentences, keywords, and FAST subjects carry source IDs and verbatim supporting excerpts. Missing/redacted details are not guessed.
- Semantic retrieval merged with SQLite FTS5 lexical retrieval over non-deleted topical and geographic FAST records. Reciprocal-rank fusion merges the routes; the existing cross-encoder reranks the pool. Unknown/deleted authority IDs and the rejected September 11 “in art” subdivision are excluded.
- The verified collection heading `September 11 Terrorist Attacks (2001)` (`fst01112794`) plus up to four specific candidate headings. Fewer than five total are allowed when the evidence does not support four additional subjects. The universal event is a cataloging policy, not an AI retrieval result.

The workbook includes supporting passages and source provenance. Full JSON additionally preserves transcript spans, frame manifests, selection rationales, retrieval routes, model usage and implementation fingerprints. API usage increases with more frames and model calls; exact counts are recorded in provenance. Previous baseline files were preserved locally under `outputs/baseline_before_robust/`.

`robust_metadata.py` implements the new workflow. Source quotes are checked literally against exact source spans; those checks validate traceability, not entailment. Audio transcription is enabled in the notebook; audio-derived emotional labels are not generated.

## Audio-generated transcripts and separate entity columns

The notebook generates interview text from audio and uses the original workbook only as the speaker-name authority. `TRANSCRIPTION_MODEL = 'gpt-transcribe'` selects the current transcription API model; `whisper-1` can be selected while that model remains available. Audio is extracted locally to mono 16 kHz MP3 and split into ten-minute chunks below the upload limit. Successful chunk transcripts are cached by full video-content SHA-256, model and settings.

The generated source workbook is `outputs/notebook/generated_transcriptions/UCFremembers911_generated_transcriptions.xlsx`. It contains one video per row with `Transcript` plus original-workbook speaker-name fields and filename-derived recording dates and transcription provenance. The notebook reads this generated Excel file back before metadata generation. Plain-text transcripts and a JSON manifest are retained beside it. Only `Q1_4` (first name), `Q1_5` (optional maiden name), and `Q1_6` (last name) are used from the original workbook. First and last name establish the authoritative speaker identity, overriding ASR spelling differences; the optional maiden-name field is preserved separately. Original interview transcript text is never used as fallback. Name provenance is recorded, and unmatched or ambiguous name rows stop the run. Speaker affiliation/occupation must now be supported by the audio-generated text; it is not copied from the supplied workbook. Automatic transcription may mishear other names or wording. Chunk starts are approximate chunk positions, not word-aligned timestamps.

The main metadata sheet exports `People`, `Locations`, `Organizations/ Initiatives`, `Dates`, `Themes` and `Perspective` as separate columns. List values use `; ` separators without JSON array notation or JSON quoting. Full structured evidence remains in the JSON output and evidence worksheets. Set `DRY_RUN=True` to transcribe and process only the first video; normal mode processes all videos.

Workbook output uses the managed Artifact Tool runtime. `workbook_io.py` discovers it under `~/.cache/codex-runtimes/codex-primary-runtime/dependencies`; set `ARTIFACT_DEPENDENCIES` if the runtime is stored elsewhere. Previous outputs from supplied transcripts are preserved locally under `outputs/before_audio_transcription/`.

### Raw visual evidence

Visual post-processing is disabled. All observations are exported unchanged, including repeated activities. The main Visual Evidence JSON column contains the original observations as validated JSON with timestamps, and Visual_Evidence contains one row per observation. There is no processed visual worksheet or processed visual object in the JSON output. Capitalized headers and semicolon-separated entity values are retained.

To refresh the README example after a new notebook run:

```sh
.venv/bin/python examples/build_readme_example.py
```

Run the local checks with `.venv/bin/python -m unittest discover -q`.

# Oral-history metadata pipeline

Generates video metadata from the six oral-history interviews. The notebook exports `outputs/notebook/UCFremembers911_video_metadata.xlsx`; the legacy script exports `outputs/video_metadata.xlsx`.

The current workflow is the notebook: it generates transcripts from video audio, extracts representative visual evidence from eight frames, and exports descriptions, separate entity facets, five keywords, and up to five supported FAST subjects. Start with [Current notebook workflow](#current-notebook-workflow). The standalone `pipeline.py` workflow below is retained as a legacy alternative.

<!-- BEGIN EXCEL VIDEO EXAMPLE -->
## Video examples — all generated results

All 6 interviews from the eight-frame notebook run. Each example includes every entity facet, available visual evidence, the JSON evidence, description, five keywords, FAST subjects, retrieved candidates, and supporting evidence. Every interview has one inline video player with play/pause and audio controls. A fallback link is provided below each player. Results use the original workbook’s speaker names.

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

<h4>People</h4><ul><li>Danna Arrieta-Ventura</li><li>Danna’s mother</li><li>Danna’s great-aunt</li><li>Danna’s former science teacher</li><li>The teacher’s friend</li></ul><h4>Locations</h4><ul><li>Huánuco, Peru</li><li>Lima, Peru</li><li>New York</li><li>World Trade Center</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>Family memories of 9/11</li><li>International and rural impact</li><li>Communication barriers</li><li>Fear and uncertainty</li><li>Cultural impact and aftermath</li><li>Community support</li></ul><h4>Perspective</h4><ul><li>A personal reflection drawing on family memories and stories from others; the speaker does not describe being present at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[98.533 s] Wears a red top with a black neckline and clear-framed glasses; no legible insignia is visible.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[14.067 s] Faces forward with mouth slightly open, as if speaking; gaze is directed toward the camera area.</li><li>[42.233 s] Leans forward and looks slightly downward, mouth open.</li><li>[142 s] Tilts head down and directs gaze below the camera; eyes appear closed or lowered.</li><li>[154.867 s] Raises gaze to face forward again, with a neutral visible expression.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Danna Arrieta-Ventura</h3><p>169 seconds · 8 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/ad0a2e53-54f9-4865-97ed-561001bc8423

<p><a href="examples/videos/danna-arrieta-ventura.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Danna Arrieta-Ventura reflects on her family’s connections to 9/11 and its aftermath in an interview recorded September 11, 2026. She describes her mother’s family as immigrants from Huánuco, Peru, and explains that her mother was studying in high school in New York in 2001. Danna recounts how her great-aunt, in Lima, followed the attacks on the radio and feared for her mother because communication between Peru and New York was limited. She also shares a story from middle school about her former science teacher’s friend, a hijab-wearing woman who worked near the World Trade Center and was hidden by coworkers and friends while walking in New York in the weeks afterward. Danna emphasizes the cultural impact and fear caused by 9/11 in the United States and internationally, including in rural areas. Her account is primarily a reflection on inherited family memories and stories she heard, rather than a description of her own presence at an attack site.</p><h4>Keywords</h4><ul><li>Family memories of 9/11</li><li>Peruvian family connections</li><li>International impact of 9/11</li><li>Communication barriers and family separation</li><li>Cultural impact and community support after 9/11</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>Peru--Huánuco</li><li>Peru--Lima</li></ul>

</td>
</tr>
</table>

<details><summary>Visual evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "frame_id": "V005",
      "category": "attire_and_symbols",
      "observation": "Wears a red top with a black neckline and clear-framed glasses; no legible insignia is visible.",
      "timestamp_seconds": 98.533
    },
    {
      "frame_id": "V001",
      "category": "activities_and_emotional_moments",
      "observation": "Faces forward with mouth slightly open, as if speaking; gaze is directed toward the camera area.",
      "timestamp_seconds": 14.067
    },
    {
      "frame_id": "V003",
      "category": "activities_and_emotional_moments",
      "observation": "Leans forward and looks slightly downward, mouth open.",
      "timestamp_seconds": 42.233
    },
    {
      "frame_id": "V007",
      "category": "activities_and_emotional_moments",
      "observation": "Tilts head down and directs gaze below the camera; eyes appear closed or lowered.",
      "timestamp_seconds": 142.0
    },
    {
      "frame_id": "V008",
      "category": "activities_and_emotional_moments",
      "observation": "Raises gaze to face forward again, with a neutral visible expression.",
      "timestamp_seconds": 154.867
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>2. Peru--Puerto Inca (Huánuco) (fst01314272)</li><li>3. Peru--Huánuco (fst01223929)</li><li>4. Peru--Santa Marta (Huánuco) (fst01319201)</li><li>5. Peru--Huánuco (Department) (fst01715148)</li><li>6. Peru--Comas (Lima : District) (fst01335220)</li><li>7. Peru--Santa María (Huánuco) (fst01322373)</li><li>8. Peru in music (fst01058918)</li><li>9. Peru--Huánuco (Diocese) (fst01336116)</li><li>10. Peru--Lima--Quinta Heeren (fst01715160)</li><li>11. Peru--Lima--Huáscar (fst01715156)</li><li>12. Peru--Lima--El Agustino (fst01715155)</li><li>13. Peru--San Bartolo (Lima) (fst01871940)</li><li>14. Peru--Chancay River (Lima) (fst01316851)</li><li>15. New York (State)--Tioga Center (fst01881448)</li><li>16. Victims of terrorism--Family relationships (fst01166348)</li><li>17. Peru--Huánuco Pampa (fst01235122)</li><li>18. Peru--Chancay (Lima) (fst01320876)</li><li>19. Peru--Lima--Barrios Altos (fst01715153)</li><li>20. Peru--Lima--Miraflores (fst01715158)</li><li>21. Peru--Huánuco Pampa Site (fst01245200)</li><li>22. Peru--Lima--San Isidro (fst01715161)</li><li>23. Huaylas (fst00962660)</li><li>24. Peru--Barranca (Lima) (fst01314882)</li><li>25. Peru--Acos (Lima) (fst01315000)</li><li>26. Peru--Lima (fst01205423)</li><li>27. Peru--Lima Region (fst01348990)</li><li>28. New York (State)--New York--World Trade Center Site (fst01328038)</li><li>29. Peru--Lima Metropolitan Area (fst01348989)</li><li>30. Peru--Lima--Pueblo Libre (fst01715159)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/danna-arrieta-ventura.json).

### Chereeka Garner

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Chereeka Garner</li><li>Garner&#x27;s father</li></ul><h4>Locations</h4><ul><li>UCF John C. Hitt Library</li><li>University High School, Orlando, Florida</li><li>World Trade Center</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF</li><li>Night Tales Project</li><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11, 2001 attacks</li><li>high school recollections</li><li>television news coverage</li><li>school dismissal and family response</li></ul><h4>Perspective</h4><ul><li>First-person recollection by a high school senior who learned about the attacks at school and watched television coverage; she does not describe being at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[6 s] The seated speaker wears a white outer layer over a dark navy top with a folded collar; no legible insignia is visible.</li></ul><p><strong>Artifacts and props</strong></p><ul><li>6 s · V001 · A large foam-covered microphone on an articulated arm is visible at the left; another microphone is partly visible at the upper right.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[50 s] The speaker looks downward with eyes partly closed and mouth open mid-speech.</li><li>[82.333 s] The speaker faces forward with eyes widened and mouth slightly open while speaking.</li><li>[192.1 s] The speaker&#x27;s brow is furrowed and eyes narrowed, with mouth open mid-speech.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Chereeka Garner</h3><p>329 seconds · 8 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/1fdbbf3b-c853-4382-88d9-0274cb13f681

<p><a href="examples/videos/chereeka-garner.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Chereeka Garner is recording an interview at UCF’s John C. Hitt Library for the Night Tales Project. She recalls being a senior at University High School in Orlando on September 11, 2001, when her class gathered to take its senior photograph. After the photo, she waited in the courtyard and then entered a classroom where students were watching television coverage of the attacks. Her history teacher told the class that a plane had hit the World Trade Center, and Garner recalls watching the news coverage for about an hour. She called her father, who told her she could go home, but a long line at the attendance office prevented her from signing out. Garner recalls remaining at school until the end of the day and understanding the magnitude of the events more fully after she got home and found her father there.</p><h4>Keywords</h4><ul><li>September 11, 2001 high school recollections</li><li>school-day response to the attacks</li><li>television news coverage of September 11</li><li>school dismissal and attendance office</li><li>family response to the attacks</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>Florida--Orlando</li></ul>

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
      "observation": "The seated speaker wears a white outer layer over a dark navy top with a folded collar; no legible insignia is visible.",
      "timestamp_seconds": 6.0
    },
    {
      "frame_id": "V001",
      "category": "artifacts_and_props",
      "observation": "A large foam-covered microphone on an articulated arm is visible at the left; another microphone is partly visible at the upper right.",
      "timestamp_seconds": 6.0
    },
    {
      "frame_id": "V003",
      "category": "activities_and_emotional_moments",
      "observation": "The speaker looks downward with eyes partly closed and mouth open mid-speech.",
      "timestamp_seconds": 50.0
    },
    {
      "frame_id": "V004",
      "category": "activities_and_emotional_moments",
      "observation": "The speaker faces forward with eyes widened and mouth slightly open while speaking.",
      "timestamp_seconds": 82.333
    },
    {
      "frame_id": "V006",
      "category": "activities_and_emotional_moments",
      "observation": "The speaker's brow is furrowed and eyes narrowed, with mouth open mid-speech.",
      "timestamp_seconds": 192.1
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. Local Library Cooperation Project (fst01001196)</li><li>2. News recordings (fst01037025)</li><li>3. Library orientation for junior high school students (fst00997856)</li><li>4. Horror tales--Library resources (fst00960394)</li><li>5. Library orientation for high school students (fst00997853)</li><li>6. School library agencies (fst01107552)</li><li>7. Television in university extension (fst01146945)</li><li>8. School library finance (fst01107553)</li><li>9. Florida--Florida State University Reservation (fst01882094)</li><li>10. Fairy tales on television (fst02021234)</li><li>11. School library supervisors (fst01107554)</li><li>12. Library orientation for high school students--Evaluation (fst00997854)</li><li>13. Library publications (fst00997882)</li><li>14. Neighborhood Information Center Project (fst01035615)</li><li>15. Library school closings (fst00997906)</li><li>16. Florida--Orlando Metropolitan Area (fst01343966)</li><li>17. Florida--North Orlando (fst01216436)</li><li>18. Florida--Orlando (fst01204036)</li><li>19. Florida--Orlando Region (fst01343967)</li><li>20. Florida--Orlando--Holy Land Experience (fst01905680)</li><li>21. Florida--Orlando--International Drive (fst01320716)</li><li>22. Florida--Orlando Suburban Area (fst01343968)</li><li>23. Florida--Tallahassee--University Park (fst01329164)</li><li>24. Florida--Orlando--Pine Castle (fst01313729)</li><li>25. Florida--Orlando--Universal Studios Florida (Amusement park) (fst01336402)</li><li>26. Florida--Orlando--Williamsburg (fst01323268)</li><li>27. Florida--John F. Kennedy Space Center Region (fst01308005)</li><li>28. High school students&#x27; writings (fst00956236)</li><li>29. Florida--Port Saint John (fst01226588)</li><li>30. Washington (D.C.)--John F. Kennedy Center Plaza (fst01327677)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/chereeka-garner.json).

### Phillip Jones

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Phillip Jones</li><li>Dwayne Williams</li></ul><h4>Locations</h4><ul><li>Shaw Air Force Base</li><li>Sumter, South Carolina</li><li>Egypt</li><li>Middle East</li><li>Afghanistan</li><li>Iraq</li><li>Pentagon</li></ul><h4>Organizations/ Initiatives</h4><ul><li>U.S. CENTAF</li><li>U.S. Air Force</li><li>UAE</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>about 90 days after September 11, 2001</li><li>about Thanksgiving</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11 attacks</li><li>television coverage</li><li>military planning and deployment</li><li>logistics and transportation</li><li>care for personnel overseas</li><li>loss and remembrance</li></ul><h4>Perspective</h4><ul><li>First-person recollection by a military planner of watching television coverage and responding from Shaw Air Force Base; the account does not describe his presence at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[25.367 s] he wears a royal-blue collared shirt and a dark navy baseball cap embroidered in yellow with “USCENTAF,” above a white aircraft graphic and smaller white lettering including “COLONEL PJ JONES.” A thin chain is visible at the neckline.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[76.133 s] his mouth is open and his gaze is angled slightly downward.</li><li>[104 s] his eyes are closed and his mouth is closed.</li><li>[177.7 s] his eyes are closed and his mouth is open, with teeth visible.</li><li>[228.467 s] his gaze is lowered and his mouth is slightly open.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Phillip Jones</h3><p>305 seconds · 8 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/df0aa204-9ee7-4d20-8c0a-789cf0a7246d

<p><a href="examples/videos/phillip-jones.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Phillip Jones, a retired Air Force colonel, recalls serving as deputy A5 at U.S. CENTAF at Shaw Air Force Base on September 11, 2001. He describes watching the second airplane strike on television and realizing the event was not an accident. Jones sent staff and conference attendees home, then helped cancel programs, arrange support for personnel in Egypt, and prepare orders to deploy forces to the Middle East. He recalls that the UAE visitors were in Sumter, South Carolina, where they had been roughed up and confined to their rooms, while the Egyptian personnel remained in Egypt. Jones says he worked for about 90 days without a day off, coordinating transportation for forces and units deploying to the Middle East, and later helped plan for Afghanistan and the Iraq war. He also remembers his friend Dwayne Williams, an Army major who perished, and reflects on the loss to Williams’s family and friends.</p><h4>Keywords</h4><ul><li>September 11 television coverage</li><li>military response planning</li><li>Middle East force deployment logistics</li><li>overseas personnel support</li><li>remembrance of a fallen friend</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>South Carolina--Shaw Air Force Base</li><li>September 11 Terrorist Attacks, 2001, on television</li></ul>

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
      "observation": "he wears a royal-blue collared shirt and a dark navy baseball cap embroidered in yellow with “USCENTAF,” above a white aircraft graphic and smaller white lettering including “COLONEL PJ JONES.” A thin chain is visible at the neckline.",
      "timestamp_seconds": 25.367
    },
    {
      "frame_id": "V003",
      "category": "activities_and_emotional_moments",
      "observation": "his mouth is open and his gaze is angled slightly downward.",
      "timestamp_seconds": 76.133
    },
    {
      "frame_id": "V004",
      "category": "activities_and_emotional_moments",
      "observation": "his eyes are closed and his mouth is closed.",
      "timestamp_seconds": 104.0
    },
    {
      "frame_id": "V006",
      "category": "activities_and_emotional_moments",
      "observation": "his eyes are closed and his mouth is open, with teeth visible.",
      "timestamp_seconds": 177.7
    },
    {
      "frame_id": "V007",
      "category": "activities_and_emotional_moments",
      "observation": "his gaze is lowered and his mouth is slightly open.",
      "timestamp_seconds": 228.467
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. South Carolina--Shaw Air Force Base (fst01219335)</li><li>2. North Carolina--Seymour Johnson Air Force Base (fst01927912)</li><li>3. South Africa--Swartkop Air Force Base (fst01877526)</li><li>4. Georgia--Moody Air Force Base (fst01204246)</li><li>5. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>6. North Carolina--Pope Air Force Base (fst01277322)</li><li>7. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>8. Texas--Bergstrom Air Force Base (fst01246199)</li><li>9. South Carolina--Myrtle Beach Air Force Base (fst01238171)</li><li>10. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>11. Virginia--Langley Air Force Base (fst01212030)</li><li>12. Georgia--Dobbins Air Force Base (fst01239332)</li><li>13. Texas--Goodfellow Air Force Base (fst01224894)</li><li>14. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>15. Alabama--Maxwell Air Force Base (fst01216242)</li><li>16. Texas--Dyess Air Force Base (fst01214180)</li><li>17. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>18. Ohio--Newark Air Force Base (fst01231899)</li><li>19. Pennsylvania--Olmsted Air Force Base (fst01253738)</li><li>20. Texas--Randolph Air Force Base (fst01213140)</li><li>21. Indiana--Grissom Air Force Base (fst01227123)</li><li>22. California--George Air Force Base (fst01222751)</li><li>23. Texas--Lackland Air Force Base (fst01229984)</li><li>24. Illinois--Chanute Air Force Base (fst01218461)</li><li>25. Alaska--Ladd Air Force Base (fst01214544)</li><li>26. Texas--Carswell Air Force Base (fst01253325)</li><li>27. California--Mather Air Force Base (fst01233944)</li><li>28. Georgia--Robins Air Force Base (fst01204249)</li><li>29. Michigan--Wurtsmith Air Force Base (fst01224831)</li><li>30. Florida--Eglin Air Force Base (fst01214481)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/phillip-jones.json).

### Ken Lundy

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Ken Lundy</li></ul><h4>Locations</h4><ul><li>UCF John C. Hitt Library</li><li>New York City</li><li>Grand Rapids, Michigan</li><li>World Trade Center</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF</li><li>Knights Tales Project</li><li>Steelcase</li><li>Social Security</li></ul><h4>Dates</h4><ul><li>September 11, 2026 (recording date)</li><li>September 11, 2001</li><li>Labor Day 2001</li></ul><h4>Themes</h4><ul><li>September 11 attacks</li><li>personal recollection</li><li>work and travel</li><li>family communication</li><li>World Trade Center visit</li><li>remembrance and healing</li></ul><h4>Perspective</h4><ul><li>First-person recollection of watching events unfold in Grand Rapids, alongside a visit to the World Trade Center on Labor Day 2001; the account does not establish that Lundy was physically present at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[15.567 s] Wearing a black collared top and large translucent, pale-framed glasses with black temples; a small white mark is visible on one temple but is not legible.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[46.733 s] Mouth open mid-speech, facing mostly forward with gaze slightly to the side.</li><li>[158 s] Gaze lowered and lips closed; no hand gesture is visible.</li><li>[171.367 s] Mouth open mid-speech, with gaze angled slightly downward to the side.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Ken Lundy</h3><p>187 seconds · 8 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/56694318-b34f-448b-ae63-0d945b35f1cf

<p><a href="examples/videos/ken-lundy.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Ken Lundy records this interview at UCF’s John C. Hitt Library for the Knights Tales Project on September 11, 2026. He describes having firsthand experience of 9/11 while working for Steelcase, whose New York City territory was his responsibility. After Labor Day 2001, he and his wife flew back to Grand Rapids, Michigan, and watched events unfold at Steelcase headquarters on September 11. He recalls being unable to reach his wife, who was working for Social Security, and meeting her at home later that afternoon. Lundy says his first visit to the World Trade Center towers was on Labor Day 2001, when he also met a friend in the shopping area and saw people who worked in the building. He closes by remembering the victims, expressing hope for healing, and saying that people will not forget.</p><h4>Keywords</h4><ul><li>September 11, 2001, personal recollections</li><li>World Trade Center visit</li><li>Grand Rapids workplace experience</li><li>family communication during the attacks</li><li>remembrance and healing</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>New York (State)--New York--World Trade Center Site</li></ul>

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
      "observation": "Wearing a black collared top and large translucent, pale-framed glasses with black temples; a small white mark is visible on one temple but is not legible.",
      "timestamp_seconds": 15.567
    },
    {
      "frame_id": "V002",
      "category": "activities_and_emotional_moments",
      "observation": "Mouth open mid-speech, facing mostly forward with gaze slightly to the side.",
      "timestamp_seconds": 46.733
    },
    {
      "frame_id": "V006",
      "category": "activities_and_emotional_moments",
      "observation": "Gaze lowered and lips closed; no hand gesture is visible.",
      "timestamp_seconds": 158.0
    },
    {
      "frame_id": "V007",
      "category": "activities_and_emotional_moments",
      "observation": "Mouth open mid-speech, with gaze angled slightly downward to the side.",
      "timestamp_seconds": 171.367
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. Local Library Cooperation Project (fst01001196)</li><li>2. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>3. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>4. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>5. Neighborhood Information Center Project (fst01035615)</li><li>6. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>7. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>8. Washington (D.C.)--John F. Kennedy Center Plaza (fst01327677)</li><li>9. September (fst01112793)</li><li>10. Virginia--John W. Warner Rapids (fst01878859)</li><li>11. Personal recordings (fst01058643)</li><li>12. Family social work (fst00920516)</li><li>13. Family social work--Study and teaching (fst00920525)</li><li>14. New York (State)--Guilderland Center (fst01229406)</li><li>15. New York (State)--New York--Grand Central Parkway (fst01922085)</li><li>16. Communication in families (fst01728100)</li><li>17. Workers&#x27; travel programs (fst01180403)</li><li>18. Family counseling (fst00920300)</li><li>19. Family social work--Research (fst00920523)</li><li>20. Communication in folklore (fst00870146)</li><li>21. New York (State)--Center Moriches (fst01257864)</li><li>22. Communication in social work (fst00870289)</li><li>23. New York (State)--New York--World Trade Center Site (fst01328038)</li><li>24. Healing in art (fst00952727)</li><li>25. Recollection (Psychology) (fst01091460)</li><li>26. New York (State)--New City (fst01256058)</li><li>27. New York (State)--Ontario Center (fst01268210)</li><li>28. Communication in family planning (fst01728103)</li><li>29. Spiritual healing (fst01130087)</li><li>30. Work and family (fst01180235)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/ken-lundy.json).

### Juan Reyes Sierra

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Juan Reyes Sierra</li><li>President Bush</li></ul><h4>Locations</h4><ul><li>UCF</li><li>Sarasota, Florida</li><li>Longboat Key, Florida</li><li>Colony Beach and Resort</li><li>Booker Elementary School</li><li>Sarasota Airport</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11, 2001</li><li>family memory</li><li>presidential visit</li><li>hotel logistics</li><li>airport shutdown and fighter jets</li><li>intergenerational remembrance</li></ul><h4>Perspective</h4><ul><li>A son recounts his father’s experience and his own inherited family memory; the speaker was not born at the time and does not describe personal presence at an attack site.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[62.5 s] He wears a dark top or jacket with a light gray-beige strap or trim visible over one shoulder; no legible insignia is visible.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[22 s] Facing forward, he looks toward the camera with his mouth slightly open.</li><li>[76 s] He turns his face down and to one side, with his gaze lowered.</li><li>[87.5 s] He bows his head, looking down; only the upper portion of his face is visible near the lower edge of the frame.</li><li>[137.5 s] Facing forward again, he looks slightly upward with his mouth open.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Juan Reyes Sierra</h3><p>150 seconds · 8 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/555a06d6-3591-4e93-af75-2a084bedf1f6

<p><a href="examples/videos/juan-reyes-sierra.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Juan Reyes Sierra, a UCF senior, shares his father’s account of being with President Bush on the morning of September 11, 2001; Reyes Sierra says he was not yet born at the time. Reyes Sierra says his father was a manager at the Colony Beach and Resort in Longboat Key, Florida, and was responsible for logistics during President Bush’s stay there before the president went to Booker Elementary School in Sarasota. According to Reyes Sierra, his father helped prepare a brunch menu for the president and took a photograph with him. Reyes Sierra recounts that his father later saw Sarasota Airport shut down and fighter jets, amid concern that the president might be targeted. Framing the account as his father’s experience rather than his own, Reyes Sierra says he feels proud to share the story and remembers his father’s lasting sense of amazement about the encounter. Recorded on September 11, 2026, this oral history is part of the UCF Remembers 9/11 collection.</p><h4>Keywords</h4><ul><li>September 11 family memories</li><li>President Bush’s Sarasota visit</li><li>hotel management and presidential logistics</li><li>Sarasota Airport shutdown and fighter jets</li><li>intergenerational remembrance of September 11</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>Florida--Sarasota</li><li>Collective memory</li></ul>

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
      "observation": "He wears a dark top or jacket with a light gray-beige strap or trim visible over one shoulder; no legible insignia is visible.",
      "timestamp_seconds": 62.5
    },
    {
      "frame_id": "V002",
      "category": "activities_and_emotional_moments",
      "observation": "Facing forward, he looks toward the camera with his mouth slightly open.",
      "timestamp_seconds": 22.0
    },
    {
      "frame_id": "V005",
      "category": "activities_and_emotional_moments",
      "observation": "He turns his face down and to one side, with his gaze lowered.",
      "timestamp_seconds": 76.0
    },
    {
      "frame_id": "V006",
      "category": "activities_and_emotional_moments",
      "observation": "He bows his head, looking down; only the upper portion of his face is visible near the lower edge of the frame.",
      "timestamp_seconds": 87.5
    },
    {
      "frame_id": "V008",
      "category": "activities_and_emotional_moments",
      "observation": "Facing forward again, he looks slightly upward with his mouth open.",
      "timestamp_seconds": 137.5
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>2. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>3. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>4. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>5. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>6. September (fst01112793)</li><li>7. Reggiane Re.2001 (Fighter plane) (fst01910112)</li><li>8. Caudron R.11 (Fighter plane) (fst01909358)</li><li>9. Jets (fst00982494)</li><li>10. Florida--Sarasota Metropolitan Area (fst01343986)</li><li>11. National Family Week (fst01033209)</li><li>12. Florida--Dania Beach (fst01216013)</li><li>13. Jet fighter planes (fst01762856)</li><li>14. Westcott Gate (Tallahassee, Fla.) (fst01762842)</li><li>15. Florida--Key West (fst01207829)</li><li>16. Florida--Madeira Beach (fst01215210)</li><li>17. LUSAC-11 (Fighter plane) (fst01746112)</li><li>18. Florida--Palm Beach (fst01215470)</li><li>19. Florida--Daytona Beach (fst01202733)</li><li>20. Florida--Apollo Beach (fst01210771)</li><li>21. Yak-9 (Fighter plane) (fst01748773)</li><li>22. Presidential trees (fst02072020)</li><li>23. Florida--Jacksonville Beach (fst01216122)</li><li>24. Florida--Atlantic Beach (fst01216138)</li><li>25. Florida--Pensacola Beach (fst01205000)</li><li>26. Florida--Miami Beach (fst01204159)</li><li>27. Florida--Pompano Beach (fst01215852)</li><li>28. Florida--Sarasota (fst01207248)</li><li>29. Florida--Vero Beach (fst01213563)</li><li>30. Collective memory (fst01739814)</li></ul>

</details>

[Full generated result and supporting evidence](examples/data/juan-reyes-sierra.json).

### Doris Stanley

<table>
<tr><th width="40%">Entities and visual evidence</th><th width="60%">Video and generated metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Doris Stanley</li></ul><h4>Locations</h4><ul><li>New York</li><li>Pennsylvania</li><li>Pentagon</li><li>UCF</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11 attacks</li><li>television coverage</li><li>restaurant work</li><li>anxiety and panic attacks</li><li>counseling</li><li>memorial visit and healing</li></ul><h4>Perspective</h4><ul><li>First-person recollection of television coverage during restaurant work, its later personal effects, and a subsequent memorial visit; no physical presence at an attack site is described.</li></ul><p><strong>Attire and symbols</strong></p><ul><li>[24.033 s] Wearing a dark, open-collar blouse; dark hair is tied back, with loose strands framing the face. No legible insignia is visible.</li></ul><p><strong>Activities, expressions and gaze</strong></p><ul><li>[2 s] holds a closed hand against the mouth and looks downward.</li><li>[46 s] mouth is slightly open and gaze is directed downward.</li><li>[216.4 s] looks forward with lips slightly parted.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Doris Stanley</h3><p>289 seconds · 8 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/f9be7b37-b4aa-41ad-bb88-7bf68a76879c

<p><a href="examples/videos/doris-stanley.mp4">Open video with audio if the inline player is unavailable</a></p><h4>Description</h4><p>Doris Stanley recalls watching television coverage of the September 11 attacks while working at a restaurant as a 21-year-old. As the restaurant prepared to open for lunch, its televisions switched to footage of the attacks in New York, Pennsylvania, and at the Pentagon. She remembers watching the World Trade Center collapse and describes feeling shocked and frightened as the footage played repeatedly. Stanley says the television coverage had effects she recognized later, including anxiety, panic attacks, and new fears of heights and driving over bridges. After coming to UCF, she used counseling services and says she connected those experiences to watching the coverage. During a later visit to New York for a conference, she went to the memorial and describes the visit as healing in some ways. Recorded September 11, 2026, this interview is part of the UCF Remembers 9/11 collection.</p><h4>Keywords</h4><ul><li>September 11 attacks and television coverage</li><li>restaurant work on September 11</li><li>anxiety and panic attacks after the attacks</li><li>UCF counseling services</li><li>New York memorial visit</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>September 11 Terrorist Attacks, 2001, on television</li><li>Panic attacks</li></ul>

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
      "observation": "Wearing a dark, open-collar blouse; dark hair is tied back, with loose strands framing the face. No legible insignia is visible.",
      "timestamp_seconds": 24.033
    },
    {
      "frame_id": "V001",
      "category": "activities_and_emotional_moments",
      "observation": "holds a closed hand against the mouth and looks downward.",
      "timestamp_seconds": 2.0
    },
    {
      "frame_id": "V003",
      "category": "activities_and_emotional_moments",
      "observation": "mouth is slightly open and gaze is directed downward.",
      "timestamp_seconds": 46.0
    },
    {
      "frame_id": "V007",
      "category": "activities_and_emotional_moments",
      "observation": "looks forward with lips slightly parted.",
      "timestamp_seconds": 216.4
    }
  ]
}
```

</details>

<details><summary>All retrieved FAST candidates</summary>

<ul><li>1. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>2. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>3. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>4. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>5. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>6. Restaurant management--Study and teaching (fst01095903)</li><li>7. Restaurant management (fst01095899)</li><li>8. Restaurant management--Periodicals (fst01095901)</li><li>9. Restaurants--Personnel management (fst01095946)</li><li>10. Restaurants--Food service (fst01095933)</li><li>11. September (fst01112793)</li><li>12. Rehabilitation counseling--Field work (fst01093359)</li><li>13. Television in counseling (fst01146878)</li><li>14. Hotel restaurants (fst01763303)</li><li>15. Restaurant management--Prices (fst01095902)</li><li>16. Counseling--Practice (fst00881230)</li><li>17. Counseling (fst00881212)</li><li>18. Family counseling (fst00920300)</li><li>19. Educational counseling (fst00903395)</li><li>20. Pentagon (fst01057151)</li><li>21. Health counseling (fst00952875)</li><li>22. Counseling--Psychological aspects (fst00881231)</li><li>23. Short-term counseling (fst01117479)</li><li>24. Panic attacks--Alternative treatment (fst01751936)</li><li>25. Panic attacks (fst01052114)</li><li>26. Counseling psychology (fst01740078)</li><li>27. Mental health counseling (fst01016395)</li><li>28. Marriage counseling (fst01010578)</li><li>29. Anxiety on television (fst02021893)</li><li>30. Television in police work (fst01146915)</li></ul>

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

The notebook now defaults to `ROBUST_MODE = True` and `ROBUST_FRAME_COUNT = 8`. Set `ROBUST_MODE = False` to use the earlier six-frame workflow. Run with:

```sh
.venv/bin/python run_notebook.py
```

The evidence-first mode adds:

- Six evenly spaced coverage frames plus two additional frames chosen from a two-second visual-change scan, up to eight total (67% fewer API images than the previous default). Images are sent at high detail, resized within 1280 × 1280 pixels. This improves coverage but cannot guarantee detection of every short event.
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

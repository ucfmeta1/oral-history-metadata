# Oral-History Metadata Pipeline

Generates video metadata from the six oral-history interviews. The notebook exports `outputs/notebook/UCFremembers911_video_metadata.xlsx`; the legacy script exports `outputs/video_metadata.xlsx`.

The current workflow is the notebook: it generates transcripts from video audio, extracts representative visual evidence from 15 frames, and exports descriptions, separate entity facets, five keywords, and up to five supported FAST subjects. Start with [Current notebook workflow](#current-notebook-workflow). The standalone `pipeline.py` workflow below is retained as a legacy alternative.

<!-- BEGIN EXCEL VIDEO EXAMPLE -->
## Video Examples — All Generated Results

All 6 interviews from the 15-frame notebook run. Each example includes every entity facet, available visual evidence, the JSON evidence, description, five keywords, FAST subjects, retrieved candidates, and supporting evidence. Every interview has one inline video player with play/pause and audio controls. A fallback link is provided below each player. Results use the original workbook’s speaker names.

- [Danna Arrieta-Ventura](#danna-arrieta-ventura)
- [Chereeka Garner](#chereeka-garner)
- [Phillip Jones](#phillip-jones)
- [Ken Lundy](#ken-lundy)
- [Juan Reyes Sierra](#juan-reyes-sierra)
- [Doris Stanley](#doris-stanley)

### Danna Arrieta-Ventura

<table>
<tr><th width="40%">Entities and Visual Evidence</th><th width="60%">Video and Metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Danna Arrieta-Ventura</li><li>Danna Arrieta-Ventura&#x27;s mother</li><li>Danna Arrieta-Ventura&#x27;s great-aunt</li><li>Danna Arrieta-Ventura&#x27;s middle-school science teacher</li><li>The teacher&#x27;s hijab-wearing friend</li></ul><h4>Locations</h4><ul><li>Peru</li><li>Huánuco</li><li>Lima</li><li>New York</li><li>World Trade Center</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>Family Immigration and Transnational Ties</li><li>Limited International Communication</li><li>Fear and Concern for Relatives</li><li>International and Community Impact of 9/11</li><li>Protection of a Hijab-Wearing Woman After 9/11</li><li>Remembrance</li></ul><h4>Perspective</h4><ul><li>A family account combining inherited memories of the great-aunt’s experience in Lima and the mother’s circumstances in New York with a story relayed by the speaker’s middle-school science teacher; the speaker does not describe being physically present at the attacks.</li></ul><p><strong>Attire & Symbols</strong></p><ul><li>[31.667 s] The seated person wears a bright red top with a black neckline and large clear-lens glasses; no legible insignia is visible.</li></ul><p><strong>Activities, Expressions, and Gaze</strong></p><ul><li>[4 s] The person looks downward with lips parted.</li><li>[31.667 s] The person faces forward with mouth open as if speaking.</li><li>[80 s] The person looks down; in later sampled frames they mostly face forward, sometimes with lips parted.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Danna Arrieta-Ventura</h3><p>169 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/ad0a2e53-54f9-4865-97ed-561001bc8423

<p><a href="examples/videos/danna-arrieta-ventura.mp4">Open Video with Audio if the Inline Player Is Unavailable</a></p><h4>Description</h4><p>Danna Arrieta-Ventura reflects on her family’s personal connections to 9/11 and its aftermath. Her mother had immigrated from Peru and was studying in high school in New York in 2001. Because communication between the family in the United States and relatives in Peru was limited, her mother spoke with them only every week or two. When the attacks happened, her great-aunt was in Lima, where people listened to the radio and followed events; she feared for the mother’s safety while unable to contact her. The speaker also recounts a middle-school science teacher’s story about a hijab-wearing friend who worked near the World Trade Center and was surrounded and hidden by coworkers and friends in New York in the weeks afterward. She describes the aftermath as having a broad cultural impact and causing fear in the United States and internationally. The recording is part of the UCF Remembers 9/11 collection and was recorded September 11, 2026.</p><h4>Keywords</h4><ul><li>Family Communication Between New York and Peru</li><li>Great-Aunt&#x27;s Fear During 9/11 in Lima</li><li>International Family Impact of 9/11</li><li>Protection of a Hijab-Wearing Woman After 9/11</li><li>Cultural Impact and Remembrance of 9/11</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>Immigrants--Family relationships</li><li>Peru--Huánuco</li></ul>

</td>
</tr>
</table>

<details><summary>Visual Evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "category": "attire_and_symbols",
      "observation": "The seated person wears a bright red top with a black neckline and large clear-lens glasses; no legible insignia is visible.",
      "timestamp_seconds": 31.667
    },
    {
      "frame_id": "V001",
      "category": "activities_and_emotional_moments",
      "observation": "The person looks downward with lips parted.",
      "timestamp_seconds": 4.0
    },
    {
      "frame_id": "V003",
      "category": "activities_and_emotional_moments",
      "observation": "The person faces forward with mouth open as if speaking.",
      "timestamp_seconds": 31.667
    },
    {
      "frame_id": "V007",
      "category": "activities_and_emotional_moments",
      "observation": "The person looks down; in later sampled frames they mostly face forward, sometimes with lips parted.",
      "timestamp_seconds": 80.0
    }
  ]
}
```

</details>

<details><summary>All Retrieved FAST Candidates</summary>

<ul><li>1. Women immigrants--Family relationships (fst01177771)</li><li>2. Immigrants--Family relationships (fst00967734)</li><li>3. Peru--Santa Marta (Huánuco) (fst01319201)</li><li>4. Peru--Puerto Inca (Huánuco) (fst01314272)</li><li>5. Peru--Santa María (Huánuco) (fst01322373)</li><li>6. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>7. Peru--Comas (Lima : District) (fst01335220)</li><li>8. Peru--Lima--Quinta Heeren (fst01715160)</li><li>9. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>10. Peru--Acos (Lima) (fst01315000)</li><li>11. Peru--San Bartolo (Lima) (fst01871940)</li><li>12. Peru--Barranca (Lima) (fst01314882)</li><li>13. Peru--Huánuco (Department) (fst01715148)</li><li>14. Peru--Huánuco Pampa Site (fst01245200)</li><li>15. Peru--Chancay (Lima) (fst01320876)</li><li>16. Peru--Huánuco (Diocese) (fst01336116)</li><li>17. Peru--Lima--El Agustino (fst01715155)</li><li>18. Peru--Huánuco Pampa (fst01235122)</li><li>19. Peru--Huánuco (fst01223929)</li><li>20. Victims of terrorism--Family relationships (fst01166348)</li><li>21. Peru--Laraos (Lima) (fst01321814)</li><li>22. Peru--Lima--Barrios Altos (fst01715153)</li><li>23. Peru--Chancay River (Lima) (fst01316851)</li><li>24. Peru--La Victoria (Lima) (fst01715157)</li><li>25. Peru--Lima (Province) (fst01331771)</li><li>26. Peru--Lima--Huáscar (fst01715156)</li><li>27. Peru--Lima Metropolitan Area (fst01348989)</li><li>28. Peru--Lima--Pueblo Libre (fst01715159)</li><li>29. Peru in music (fst01058918)</li><li>30. Peru--Lima--Centro Histórico de Lima (fst01324518)</li></ul>

</details>

[Full Result and Supporting Evidence](examples/data/danna-arrieta-ventura.json).

### Chereeka Garner

<table>
<tr><th width="40%">Entities and Visual Evidence</th><th width="60%">Video and Metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Chereeka Garner</li><li>Garner&#x27;s father</li></ul><h4>Locations</h4><ul><li>Orlando, Florida</li><li>University High School</li><li>University of Central Florida</li><li>John C. Hitt Library</li><li>World Trade Center</li></ul><h4>Organizations/ Initiatives</h4><ul><li>Night Tales Project</li><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11 Attacks</li><li>High School Recollections</li><li>School-Day Disruption</li><li>Television News Coverage</li><li>Family Response</li><li>Senior Class Photograph</li></ul><h4>Perspective</h4><ul><li>Personal recollection of experiencing the school-day disruption and learning about the attacks through a teacher and television coverage; the speaker does not describe being physically present at an attack site.</li></ul><p><strong>Attire & Symbols</strong></p><ul><li>[6 s] The seated speaker wears a white outer layer over a dark navy top with a broad folded collar; no legible insignia is visible.</li></ul><p><strong>Artifacts & Props</strong></p><ul><li>[6 s] A large gray microphone on an adjustable arm extends into the foreground from the left; a second microphone is visible at the upper right. No handheld phone, photograph, or document is visible.</li></ul><p><strong>Activities, Expressions, and Gaze</strong></p><ul><li>[40 s] The speaker faces forward with mouth open mid-speech and eyes directed toward the camera.</li><li>[102.9 s] The speaker briefly narrows her eyes and tightens her mouth while continuing to address the camera.</li><li>[185.233 s] While speaking, the speaker glances upward and to her left rather than directly toward the camera.</li><li>[226.4 s] The speaker looks forward with widened eyes and rounded, open lips mid-speech.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Chereeka Garner</h3><p>329 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/1fdbbf3b-c853-4382-88d9-0274cb13f681

<p><a href="examples/videos/chereeka-garner.mp4">Open Video with Audio if the Inline Player Is Unavailable</a></p><h4>Description</h4><p>Chereeka Garner recalls being a high school senior in Orlando, Florida, on September 11, 2001, when her school was preparing to take the senior class photograph. After helping clean up following the photograph, she waited in the courtyard and became confused when the usual school bell did not ring. She walked to class and found students watching television; her history teacher told the class that a plane had hit the World Trade Center. Garner describes watching repeated news coverage, finding the school unusually quiet, and calling her father, who was working at the time. She recalls seeing a long line of parents signing students out, then staying at school until the end of the day before understanding the event’s magnitude at home. The interview was recorded at John C. Hitt Library for the Night Tales Project on September 11, 2026. This interview is part of the UCF Remembers 9/11 collection.</p><h4>Keywords</h4><ul><li>September 11, 2001 Recollections</li><li>High School on September 11</li><li>Television News Coverage of the Attacks</li><li>School Dismissal and Family Response</li><li>Senior Class Photograph</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>Florida--Orlando</li><li>High school seniors</li><li>September 11 Terrorist Attacks, 2001, on television</li></ul>

</td>
</tr>
</table>

<details><summary>Visual Evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "category": "attire_and_symbols",
      "observation": "The seated speaker wears a white outer layer over a dark navy top with a broad folded collar; no legible insignia is visible.",
      "timestamp_seconds": 6.0
    },
    {
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

<details><summary>All Retrieved FAST Candidates</summary>

<ul><li>1. Florida--Orlando Metropolitan Area (fst01343966)</li><li>2. Florida--North Orlando (fst01216436)</li><li>3. Florida--Orlando Suburban Area (fst01343968)</li><li>4. Florida--Orlando Region (fst01343967)</li><li>5. Florida--Orlando--Universal Studios Florida (Amusement park) (fst01336402)</li><li>6. Florida--Orlando (fst01204036)</li><li>7. Florida--Orlando--Holy Land Experience (fst01905680)</li><li>8. Florida--Orlando--International Drive (fst01320716)</li><li>9. Florida--Orlando--Pine Castle (fst01313729)</li><li>10. Florida--Orlando--Williamsburg (fst01323268)</li><li>11. High school seniors (fst00956161)</li><li>12. High school seniors--Recreation (fst00956171)</li><li>13. Orlando (Fictitious character : Shakespeare) (fst01765117)</li><li>14. Florida--High Springs (fst01214683)</li><li>15. Florida--Florida State University Reservation (fst01882094)</li><li>16. Florida--Tallahassee--University Park (fst01329164)</li><li>17. Florida--Center Hill (fst01215369)</li><li>18. Florida--Sun City Center (fst01215348)</li><li>19. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>20. Florida--Fort Center Site (fst01239603)</li><li>21. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>22. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>23. Florida--EPCOT Center (fst01244602)</li><li>24. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>25. Florida--Pine Island Center (fst01288418)</li><li>26. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>27. National Senior Citizens Day (fst01033282)</li><li>28. Florida--Port Saint John (fst01226588)</li><li>29. High school students--Social life and customs (fst00956223)</li><li>30. Library orientation for high school students--Evaluation (fst00997854)</li></ul>

</details>

[Full Result and Supporting Evidence](examples/data/chereeka-garner.json).

### Phillip Jones

<table>
<tr><th width="40%">Entities and Visual Evidence</th><th width="60%">Video and Metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Phillip Jones</li><li>Dwayne Williams</li></ul><h4>Locations</h4><ul><li>Shaw Air Force Base</li><li>Egypt</li><li>United Arab Emirates</li><li>Sumter, South Carolina</li><li>Middle East</li><li>Pentagon</li></ul><h4>Organizations/ Initiatives</h4><ul><li>U.S. CENTAF</li><li>Air Force</li><li>U.S. Army</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>About 90 days after September 11, 2001</li><li>Around Thanksgiving</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>Television Coverage of the September 11 Attacks</li><li>Military Planning and Response</li><li>Evacuation and Support for Personnel Overseas</li><li>Deployment Logistics</li><li>Personal Loss and Remembrance</li></ul><h4>Perspective</h4><ul><li>First-person account of military planning and logistics after learning of the attacks through television coverage; the speaker does not describe being at an attack site.</li></ul><p><strong>Attire & Symbols</strong></p><ul><li>[19.033 s] The man wears a royal-blue collared shirt and a dark navy cap. The cap has yellow “USCENTAF” lettering above a white airplane graphic and smaller white text reading “COLONEL PJ JONES” and “1974–2000.”</li></ul><p><strong>Activities, Expressions, and Gaze</strong></p><ul><li>[19.033 s] He faces forward with his gaze toward the camera and lips slightly parted.</li><li>[32 s] His mouth is open, showing his teeth, while his gaze is directed slightly downward.</li><li>[152 s] His head is lowered and his eyes are closed; his mouth is open.</li><li>[300 s] He looks downward with his mouth closed.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Phillip Jones</h3><p>305 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/df0aa204-9ee7-4d20-8c0a-789cf0a7246d

<p><a href="examples/videos/phillip-jones.mp4">Open Video with Audio if the Inline Player Is Unavailable</a></p><h4>Description</h4><p>Phillip Jones, a retired Air Force colonel, recounts his work as deputy A5 at U.S. CENTAF at Shaw Air Force Base on September 11, 2001. He describes learning of the attacks through office television coverage, then sending staff and conference attendees home because he feared their planning work could make them a target. Jones recounts coordinating support for personnel in Egypt and arranging military transport for them and visitors from the United Arab Emirates who had been sent to a hotel in Sumter, South Carolina. He describes the ensuing work at headquarters, including planning deployments to the Middle East and coordinating transportation for forces and units. Jones says he worked without a day off for about 90 days, until around Thanksgiving, and later contributed to planning related to Afghanistan and the war in Iraq. He closes by remembering his friend Dwayne Williams, who perished in the attacks. The recording is dated September 11, 2026.</p><h4>Keywords</h4><ul><li>Military Response Planning After September 11</li><li>Middle East Deployment Logistics</li><li>Support for Personnel Stranded Overseas</li><li>Television Coverage of the Attacks</li><li>Military Transportation Coordination</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>Transportation, Military--Planning</li><li>South Carolina--Shaw Air Force Base</li><li>South Carolina--Sumter</li></ul>

</td>
</tr>
</table>

<details><summary>Visual Evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "category": "attire_and_symbols",
      "observation": "The man wears a royal-blue collared shirt and a dark navy cap. The cap has yellow “USCENTAF” lettering above a white airplane graphic and smaller white text reading “COLONEL PJ JONES” and “1974–2000.”",
      "timestamp_seconds": 19.033
    },
    {
      "frame_id": "V001",
      "category": "activities_and_emotional_moments",
      "observation": "He faces forward with his gaze toward the camera and lips slightly parted.",
      "timestamp_seconds": 19.033
    },
    {
      "frame_id": "V002",
      "category": "activities_and_emotional_moments",
      "observation": "His mouth is open, showing his teeth, while his gaze is directed slightly downward.",
      "timestamp_seconds": 32.0
    },
    {
      "frame_id": "V008",
      "category": "activities_and_emotional_moments",
      "observation": "His head is lowered and his eyes are closed; his mouth is open.",
      "timestamp_seconds": 152.0
    },
    {
      "frame_id": "V015",
      "category": "activities_and_emotional_moments",
      "observation": "He looks downward with his mouth closed.",
      "timestamp_seconds": 300.0
    }
  ]
}
```

</details>

<details><summary>All Retrieved FAST Candidates</summary>

<ul><li>1. South Carolina--Shaw Air Force Base (fst01219335)</li><li>2. North Carolina--Pope Air Force Base (fst01277322)</li><li>3. South Carolina--Myrtle Beach Air Force Base (fst01238171)</li><li>4. North Carolina--Seymour Johnson Air Force Base (fst01927912)</li><li>5. Florida--Tyndall Air Force Base (fst01206061)</li><li>6. Texas--Dyess Air Force Base (fst01214180)</li><li>7. South Carolina--Charleston Army Air Field (fst01879374)</li><li>8. Texas--Randolph Air Force Base (fst01213140)</li><li>9. South Dakota--Ellsworth Air Force Base (fst01271967)</li><li>10. Virginia--Langley Air Force Base (fst01212030)</li><li>11. Arizona--Williams Air Force Base (fst01209443)</li><li>12. California--Vandenberg Air Force Base (fst01210320)</li><li>13. Texas--Brooks Air Force Base (fst01213141)</li><li>14. Colorado--Lowry Air Force Base (fst01213053)</li><li>15. Georgia--Moody Air Force Base (fst01204246)</li><li>16. Texas--Kelly Air Force Base (fst01212914)</li><li>17. Nevada--Nellis Air Force Base (fst01203478)</li><li>18. Transportation, Military--Planning (fst01155405)</li><li>19. California--Beale Air Force Base (fst01206542)</li><li>20. Georgia--Robins Air Force Base (fst01204249)</li><li>21. California--Norton Air Force Base (fst01212905)</li><li>22. Utah--Hill Air Force Base (fst01207125)</li><li>23. South Africa--Swartkop Air Force Base (fst01877526)</li><li>24. Arizona--Luke Air Force Base (fst01207641)</li><li>25. Nebraska--Alliance Army Air Base (fst01301519)</li><li>26. Louisiana--DeRidder Army Air Base (fst01889362)</li><li>27. South Dakota--Sioux Falls Army Air Base (fst01261021)</li><li>28. South Carolina--Sumter (fst01216215)</li><li>29. Transport of sick and wounded (fst01154957)</li><li>30. Nevada--Reno Army Air Base (fst01304129)</li></ul>

</details>

[Full Result and Supporting Evidence](examples/data/phillip-jones.json).

### Ken Lundy

<table>
<tr><th width="40%">Entities and Visual Evidence</th><th width="60%">Video and Metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Ken Lundy</li></ul><h4>Locations</h4><ul><li>John C. Hitt Library</li><li>Grand Rapids, Michigan</li><li>New York City</li><li>World Trade Center</li></ul><h4>Organizations/ Initiatives</h4><ul><li>University of Central Florida</li><li>Knights Tales Project</li><li>Steelcase</li><li>Social Security</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>Labor Day 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11 Attacks</li><li>Work and Employment</li><li>Prior Visit to the World Trade Center</li><li>Remembrance and Healing</li></ul><h4>Perspective</h4><ul><li>First-person recollection of watching events unfold at Steelcase headquarters in Grand Rapids and of a prior visit to the World Trade Center; the account does not place Lundy at the attack site on September 11.</li></ul><p><strong>Attire & Symbols</strong></p><ul><li>[26 s] The man wears a black collared shirt and large, translucent light-colored rectangular glasses with dark temples; no clear insignia is visible.</li></ul><p><strong>Activities, Expressions, and Gaze</strong></p><ul><li>[74 s] He faces forward with his mouth open and teeth visible, as if speaking; his gaze is slightly lowered.</li><li>[128.533 s] He smiles broadly with teeth visible, looking slightly downward through his glasses.</li><li>[4 s] He turns his face and gaze to the right of the frame, with his mouth slightly open.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Ken Lundy</h3><p>187 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/56694318-b34f-448b-ae63-0d945b35f1cf

<p><a href="examples/videos/ken-lundy.mp4">Open Video with Audio if the Inline Player Is Unavailable</a></p><h4>Description</h4><p>Ken Lundy records this interview at John C. Hitt Library for the Knights Tales Project on September 11, 2026. He recalls working for Steelcase, whose headquarters was in Grand Rapids, Michigan, while his territory was New York City. On Labor Day 2001, Lundy and his wife had visited the New York City area to seek employment and find a place to stay; he recalls that this was his first time in the World Trade Center towers. On September 11, 2001, Lundy was back in Grand Rapids at Steelcase headquarters, where he watched events unfold and was unable to reach his wife, who was working for Social Security. He recalls meeting a friend in the World Trade Center shopping area during the earlier visit and seeing people who worked in the building. Lundy closes by remembering the victims and expressing hope for healing.</p><h4>Keywords</h4><ul><li>September 11, 2001 Attacks</li><li>World Trade Center Visit</li><li>Steelcase Headquarters in Grand Rapids</li><li>New York City Employment Search</li><li>Remembrance and Healing for 9/11 Victims</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li></ul>

</td>
</tr>
</table>

<details><summary>Visual Evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "category": "attire_and_symbols",
      "observation": "The man wears a black collared shirt and large, translucent light-colored rectangular glasses with dark temples; no clear insignia is visible.",
      "timestamp_seconds": 26.0
    },
    {
      "frame_id": "V006",
      "category": "activities_and_emotional_moments",
      "observation": "He faces forward with his mouth open and teeth visible, as if speaking; his gaze is slightly lowered.",
      "timestamp_seconds": 74.0
    },
    {
      "frame_id": "V011",
      "category": "activities_and_emotional_moments",
      "observation": "He smiles broadly with teeth visible, looking slightly downward through his glasses.",
      "timestamp_seconds": 128.533
    },
    {
      "frame_id": "V001",
      "category": "activities_and_emotional_moments",
      "observation": "He turns his face and gaze to the right of the frame, with his mouth slightly open.",
      "timestamp_seconds": 4.0
    }
  ]
}
```

</details>

<details><summary>All Retrieved FAST Candidates</summary>

<ul><li>1. Local Library Cooperation Project (fst01001196)</li><li>2. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>3. Horror tales--Library resources (fst00960394)</li><li>4. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>5. Library publications (fst00997882)</li><li>6. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>7. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>8. Library orientation for college students--Information services (fst00997850)</li><li>9. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>10. Virginia--John W. Warner Rapids (fst01878859)</li><li>11. Undergraduate libraries (fst01160892)</li><li>12. Neighborhood Information Center Project (fst01035615)</li><li>13. Michigan--Grand Rapids Metropolitan Area (fst01347388)</li><li>14. Ohio--Grand Rapids (Township) (fst01336664)</li><li>15. Research libraries (fst01095327)</li><li>16. Michigan--Grand Rapids (Township) (fst01337295)</li><li>17. Wisconsin--Grand Rapids (Town) (fst01334115)</li><li>18. Libraries--Special collections--College publications (fst02029811)</li><li>19. September (fst01112793)</li><li>20. Washington (D.C.)--John F. Kennedy Center Plaza (fst01327677)</li><li>21. North Dakota--Grand Rapids (fst01280194)</li><li>22. Manitoba--Grand Rapids (fst01341467)</li><li>23. Michigan--Grand Rapids Suburban Area (fst01347390)</li><li>24. Manitoba--Little Grand Rapids (fst01341345)</li><li>25. Michigan--Grand Rapids Region (fst01347389)</li><li>26. Michigan--East Grand Rapids (fst01232068)</li><li>27. World politics--Library resources (fst01181393)</li><li>28. New York (State)--New York--Grand Central Parkway (fst01922085)</li><li>29. Michigan--Grand Rapids--Heritage Hill (fst01712102)</li><li>30. Ohio--Grand Rapids (fst01291166)</li></ul>

</details>

[Full Result and Supporting Evidence](examples/data/ken-lundy.json).

### Juan Reyes Sierra

<table>
<tr><th width="40%">Entities and Visual Evidence</th><th width="60%">Video and Metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Juan Reyes Sierra</li><li>Juan Reyes Sierra&#x27;s father</li><li>George W. Bush</li></ul><h4>Locations</h4><ul><li>University of Central Florida</li><li>Sarasota, Florida</li><li>Longboat Key, Florida</li><li>Colony Beach and Resort</li><li>Booker Elementary School</li><li>Sarasota Airport</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF Remembers 9/11</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11 Attacks</li><li>Family Memory</li><li>Presidential Visit</li><li>Hospitality and Event Logistics</li><li>Sarasota Response and Airport Shutdown</li><li>Intergenerational Remembrance</li></ul><h4>Perspective</h4><ul><li>A UCF student&#x27;s inherited family account of his father&#x27;s work during President Bush&#x27;s Sarasota-area visit on September 11, 2001; the speaker was not yet born and does not claim personal presence at the events.</li></ul><p><strong>Attire & Symbols</strong></p><ul><li>[22 s] The seated person wears a dark jacket over a black top, with a light gray strap visible over one shoulder; no legible insignia is visible.</li></ul><p><strong>Artifacts & Props</strong></p><ul><li>[110 s] A small black microphone with a fuzzy windscreen is visible below the person&#x27;s chin.</li><li>[90 s] A hand holds a black smartphone close to the camera. Its screen shows a photograph of two people wearing white shirts and ties, one dark and one red; the pictured people are not identified.</li></ul><p><strong>Activities, Expressions, and Gaze</strong></p><ul><li>[16 s] The person faces forward with mouth open and gaze angled slightly upward.</li><li>[46.867 s] The person lowers their head and looks down.</li><li>[90 s] The person raises the phone toward the camera while looking forward.</li><li>[96 s] The person looks upward with eyes wide and mouth slightly open.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Juan Reyes Sierra</h3><p>150 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/555a06d6-3591-4e93-af75-2a084bedf1f6

<p><a href="examples/videos/juan-reyes-sierra.mp4">Open Video with Audio if the Inline Player Is Unavailable</a></p><h4>Description</h4><p>Juan Reyes Sierra, a UCF senior, shares his father’s account of September 11, 2001, noting that he was not yet born when the attacks occurred. At the time, his father managed the Colony Beach and Resort in Longboat Key, Florida, and was responsible for logistics during President George W. Bush’s visit there on the morning of September 11. Reyes Sierra says his father recalled preparing a brunch menu for the visit and having his photograph taken with the president. His father later observed that Sarasota Airport had shut down and that fighter jets were present, amid concern that the president might be targeted. The account is inherited family memory rather than Reyes Sierra’s personal experience of 9/11; he describes feeling proud to share his father’s story. In the recording, Reyes Sierra holds up a phone displaying a photograph of two people in shirts and ties; the people shown are not identified by the visual evidence.</p><h4>Keywords</h4><ul><li>September 11, 2001 Family Memory</li><li>President Bush&#x27;s Sarasota-Area Visit</li><li>Colony Beach and Resort Logistics</li><li>Sarasota Airport Shutdown and Fighter Jets</li><li>Intergenerational Remembrance</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>Florida--Sarasota</li></ul>

</td>
</tr>
</table>

<details><summary>Visual Evidence JSON</summary>

```json
{
  "visual_observations": [
    {
      "category": "attire_and_symbols",
      "observation": "The seated person wears a dark jacket over a black top, with a light gray strap visible over one shoulder; no legible insignia is visible.",
      "timestamp_seconds": 22.0
    },
    {
      "category": "artifacts_and_props",
      "observation": "A small black microphone with a fuzzy windscreen is visible below the person's chin.",
      "timestamp_seconds": 110.0
    },
    {
      "category": "artifacts_and_props",
      "observation": "A hand holds a black smartphone close to the camera. Its screen shows a photograph of two people wearing white shirts and ties, one dark and one red; the pictured people are not identified.",
      "timestamp_seconds": 90.0
    },
    {
      "frame_id": "V003",
      "category": "activities_and_emotional_moments",
      "observation": "The person faces forward with mouth open and gaze angled slightly upward.",
      "timestamp_seconds": 16.0
    },
    {
      "frame_id": "V006",
      "category": "activities_and_emotional_moments",
      "observation": "The person lowers their head and looks down.",
      "timestamp_seconds": 46.867
    },
    {
      "frame_id": "V010",
      "category": "activities_and_emotional_moments",
      "observation": "The person raises the phone toward the camera while looking forward.",
      "timestamp_seconds": 90.0
    },
    {
      "frame_id": "V011",
      "category": "activities_and_emotional_moments",
      "observation": "The person looks upward with eyes wide and mouth slightly open.",
      "timestamp_seconds": 96.0
    }
  ]
}
```

</details>

<details><summary>All Retrieved FAST Candidates</summary>

<ul><li>1. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>2. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>3. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>4. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>5. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>6. Florida--Sarasota (fst01207248)</li><li>7. Florida--Sarasota Metropolitan Area (fst01343986)</li><li>8. September (fst01112793)</li><li>9. Hijacking of aircraft (fst00956749)</li><li>10. Florida--Sarasota Region (fst01343987)</li><li>11. Florida--Sarasota Bay Region (fst01343985)</li><li>12. Florida--Sarasota Bay Watershed (fst01877821)</li><li>13. Florida--Sarasota County (fst01214943)</li><li>14. Logistics (fst01002084)</li><li>15. Florida--Vero Beach (fst01213563)</li><li>16. Florida--Manasota Key (fst01308766)</li><li>17. Florida--Dania Beach (fst01216013)</li><li>18. Airport authorities (fst00803678)</li><li>19. Florida--Pompano Beach (fst01215852)</li><li>20. Florida--Melbourne Beach (fst01226608)</li><li>21. Florida--Madeira Beach (fst01215210)</li><li>22. Florida--Conch Key (fst01886640)</li><li>23. Florida--Jupiter Inlet Colony (fst01232504)</li><li>24. Florida--Deerfield Beach (fst01226584)</li><li>25. Florida--Siesta Key (fst01215775)</li><li>26. Florida--Lido Key (fst01241082)</li><li>27. Victims of terrorism (fst01166347)</li><li>28. Florida--Key Largo (fst01219956)</li><li>29. Florida--Delray Beach (fst01215440)</li><li>30. Florida--Palm Beach (fst01215470)</li></ul>

</details>

[Full Result and Supporting Evidence](examples/data/juan-reyes-sierra.json).

### Doris Stanley

<table>
<tr><th width="40%">Entities and Visual Evidence</th><th width="60%">Video and Metadata</th></tr>
<tr>
<td width="40%" valign="top">

<h4>People</h4><ul><li>Doris Stanley</li></ul><h4>Locations</h4><ul><li>New York</li><li>Pennsylvania</li><li>The Pentagon</li><li>University of Central Florida</li></ul><h4>Organizations/ Initiatives</h4><ul><li>UCF Remembers 9/11</li><li>University of Central Florida</li></ul><h4>Dates</h4><ul><li>September 11, 2001</li><li>September 11, 2026</li></ul><h4>Themes</h4><ul><li>September 11 Attacks</li><li>Television Coverage</li><li>Workplace Response</li><li>Anxiety and Trauma</li><li>Counseling</li><li>Memorial Visit and Healing</li><li>Collective Loss and Remembrance</li></ul><h4>Perspective</h4><ul><li>Personal recollection of watching television coverage of the attacks while at work, and reflection on their lasting effects; she does not describe being physically present at an attack site.</li></ul><p><strong>Attire & Symbols</strong></p><ul><li>[18.033 s] She wears a dark, collared, button-front shirt; no legible insignia is visible.</li></ul><p><strong>Activities, Expressions, and Gaze</strong></p><ul><li>[2 s] She holds a hand over her mouth and looks forward.</li><li>[126.233 s] She lowers her head and looks down; this downward gaze recurs in later frames.</li><li>[90.167 s] She faces forward with a visible smile.</li><li>[198.367 s] She turns her gaze to her left and slightly downward.</li></ul>

</td>
<td width="60%" valign="top">

<h3>Doris Stanley</h3><p>289 seconds · 15 sampled frames</p><p>Play/pause and audio controls are available below.</p>

https://github.com/user-attachments/assets/f9be7b37-b4aa-41ad-bb88-7bf68a76879c

<p><a href="examples/videos/doris-stanley.mp4">Open Video with Audio if the Inline Player Is Unavailable</a></p><h4>Description</h4><p>Doris Stanley recalls learning of the September 11, 2001 attacks while working at a restaurant that was preparing to open for lunch. She describes televisions in the restaurant switching to coverage of the attacks in New York, the Pentagon, and Pennsylvania, which the staff watched while preparing for the day. Stanley recalls watching the World Trade Center collapse live on television and feeling shocked and frightened by the repeated coverage. She connects the hours of televised coverage with anxiety and panic attacks that followed, and says counseling services at UCF helped her explore that impact. During a later trip to New York for a conference, she visited the memorial and describes the experience as healing in some ways. Recorded for the UCF Remembers 9/11 collection on September 11, 2026, her account reflects on the lasting effects of witnessing the attacks through television coverage.</p><h4>Keywords</h4><ul><li>September 11 Attacks and Television Coverage</li><li>Workplace Response During the Attacks</li><li>Anxiety, Panic Attacks, and Counseling</li><li>Memorial Visit and Healing</li><li>Remembrance and Collective Loss</li></ul><h4>FAST Subjects</h4><ul><li>September 11 Terrorist Attacks (2001)</li><li>September 11 Terrorist Attacks, 2001, on television</li><li>Anxiety</li><li>Traumatism--Psychological aspects</li></ul>

</td>
</tr>
</table>

<details><summary>Visual Evidence JSON</summary>

```json
{
  "visual_observations": [
    {
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

<details><summary>All Retrieved FAST Candidates</summary>

<ul><li>1. September 11 Terrorist Attacks (2001) in literature (fst01907194)</li><li>2. September 11 Terrorist Attacks, 2001, on television (fst01747281)</li><li>3. September 11 Terrorist Attacks, 2001, in comics (fst02060917)</li><li>4. September 11 Terrorist Attacks (2001) in mass media (fst01907195)</li><li>5. September 11 Terrorist Attacks (2001) in motion pictures (fst01907196)</li><li>6. September (fst01112793)</li><li>7. Pentagon in architecture (fst01057152)</li><li>8. Pentagon (fst01057151)</li><li>9. Pentagon in art (fst01057153)</li><li>10. Counseling--Practice (fst00881230)</li><li>11. Television in counseling (fst01146878)</li><li>12. Counseling--Psychological aspects (fst00881231)</li><li>13. Educational counseling (fst00903395)</li><li>14. Counseling (fst00881212)</li><li>15. Short-term counseling (fst01117479)</li><li>16. Counseling psychology (fst01740078)</li><li>17. Family counseling (fst00920300)</li><li>18. Mental health counseling (fst01016395)</li><li>19. Pentagon Memorial (Va.) (fst01200546)</li><li>20. Workplace literacy (fst01180680)</li><li>21. Health counseling (fst00952875)</li><li>22. Anxiety on television (fst02021893)</li><li>23. Pennsylvania--York (fst01202834)</li><li>24. Anxiety disorders (fst01738149)</li><li>25. Healing in the Bible (fst00952729)</li><li>26. Television and the arts (fst01146696)</li><li>27. Anxiety (fst00810950)</li><li>28. Television and the blind (fst01146697)</li><li>29. Traumatism--Psychological aspects (fst01155548)</li><li>30. Collective memory and television (fst02021907)</li></ul>

</details>

[Full Result and Supporting Evidence](examples/data/doris-stanley.json).

Source: notebook metadata records. Visual observations are retained without post-processing.
<!-- END EXCEL VIDEO EXAMPLE -->

## Legacy Script Setup and Run

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python pipeline.py --check
.venv/bin/python pipeline.py
```

The featured interview is hosted as a GitHub video attachment. Compressed viewing copies for all six interviews are included under `examples/videos/`; the original collection inputs and authority data are not distributed in this repository. Place one transcript workbook and its MP4 files under `Library-Metadata/`, topical authority JSONL under `Topical/`, and geographic authority JSONL under `Geo/`. Each authority record must contain `id`, `fast` (the authorized heading), and `deleted` fields. The workbook must retain `ResponseId`, `Q1_4` (first name), `Q1_6` (last name), and `Q14_Video_Transcript` columns. Video filenames must include the matching first and last names.

Put the OpenAI API key in `secret.txt` or `secrets.txt`, or set `OPENAI_API_KEY`. Keys are never printed. Running the pipeline sends the interview transcript and sampled frames to OpenAI and incurs API charges. Responses use `store=False`.

Defaults: `gpt-4.1-mini`, 12 evenly spaced low-detail JPEG frames per video, two GPT requests per interview. Override with `--model`, `--frames`, or `--limit 1` for a trial. Existing transcripts avoid transcription charges. Actual token usage is saved in the workbook and JSON; no fixed cost estimate is promised.

## Legacy Script Workflow

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

## Current Notebook Workflow

`Test_UCFremembers911_video_FAST_metadata.ipynb` is adapted for local execution. It uses GPT-6 Luna with model-compatible API parameters, revised rubric prompts, and the topical FAISS index (`text-embedding-3-large`), MMR retrieval, and cross-encoder reranking. It uses `secret.txt` / `secrets.txt` or `OPENAI_API_KEY` and the `.venv` environment, with no Colab dependency.

```sh
.venv/bin/python -m pip install -r requirements-notebook.txt
.venv/bin/python run_notebook.py
```

Edit configuration cell 5 (`ROOT`, `OUTPUT_DIR`, `TRANSCRIPT_WORKBOOK`, `FAST_DB_DIR`) for a different collection. Audio-generated transcripts are written to `TRANSCRIPT_WORKBOOK` and read back for name-based matching; `NAME_AUTHORITY_WORKBOOK` identifies the original workbook used only for speaker-name fields (`Q1_4`–`Q1_6`). The notebook exports 30 reranked candidates, five selected headings and five keywords for each video to `outputs/notebook/`, including Excel, CSV, JSON and an executed notebook. On first run the cross-encoder is downloaded; the local FAST index takes several GB of memory. A full run incurs transcription, configured metadata-model, and embedding API charges; cached successful stages are reused. The notebook preserves supplied redactions.

## Robust Metadata Mode

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

## Audio-Generated Transcripts and Separate Entity Columns

The notebook generates interview text from audio and uses the original workbook only as the speaker-name authority. `TRANSCRIPTION_MODEL = 'gpt-transcribe'` selects the current transcription API model; `whisper-1` can be selected while that model remains available. Audio is extracted locally to mono 16 kHz MP3 and split into ten-minute chunks below the upload limit. Successful chunk transcripts are cached by full video-content SHA-256, model and settings.

The generated source workbook is `outputs/notebook/generated_transcriptions/UCFremembers911_generated_transcriptions.xlsx`. It contains one video per row with `Transcript` plus original-workbook speaker-name fields and filename-derived recording dates and transcription provenance. The notebook reads this generated Excel file back before metadata generation. Plain-text transcripts and a JSON manifest are retained beside it. Only `Q1_4` (first name), `Q1_5` (optional maiden name), and `Q1_6` (last name) are used from the original workbook. First and last name establish the authoritative speaker identity, overriding ASR spelling differences; the optional maiden-name field is preserved separately. Original interview transcript text is never used as fallback. Name provenance is recorded, and unmatched or ambiguous name rows stop the run. Speaker affiliation/occupation must now be supported by the audio-generated text; it is not copied from the supplied workbook. Automatic transcription may mishear other names or wording. Chunk starts are approximate chunk positions, not word-aligned timestamps.

The main metadata sheet exports `People`, `Locations`, `Organizations/ Initiatives`, `Dates`, `Themes` and `Perspective` as separate columns. List values use `; ` separators without JSON array notation or JSON quoting. Dates use written month names, such as `September 11, 2026`. Themes use title case, and observation sentences begin with a capital letter. Full structured evidence remains in the JSON output and evidence worksheets. Set `DRY_RUN=True` to transcribe and process only the first video; normal mode processes all videos.

Workbook output uses the managed Artifact Tool runtime. `workbook_io.py` discovers it under `~/.cache/codex-runtimes/codex-primary-runtime/dependencies`; set `ARTIFACT_DEPENDENCIES` if the runtime is stored elsewhere. Previous outputs from supplied transcripts are preserved locally under `outputs/before_audio_transcription/`.

### Raw Visual Evidence

Visual observation content is retained without filtering, grouping, or summarization. Display capitalization is normalized. The main Visual Evidence JSON column contains the original observations as validated JSON with timestamps, and Visual_Evidence contains one row per observation. There is no processed visual worksheet or processed visual object in the JSON output. Capitalized headers and semicolon-separated entity values are retained.

To refresh the README example after a new notebook run:

```sh
.venv/bin/python examples/build_readme_example.py
```

Run the local checks with `.venv/bin/python -m unittest discover -q`.

README attire and artifact entries show bracketed timestamps (for example, `[98.533 s]`) without frame IDs. Their headings are **Attire & Symbols** and **Artifacts & Props**.

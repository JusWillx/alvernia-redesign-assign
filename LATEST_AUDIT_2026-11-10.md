# Historical accuracy audit — November 10, 2026

## What was actually checked and changed

The website now includes independently sourced 2017 men's sprint/jump/relay marks, 2018 women's shot/triple jump/javelin marks, and 2019 men's long jump and javelin marks. Mylina Castillo's indoor and outdoor triple jump bests were assigned to **2023** by checking their dates in her TFRRS athlete history (rather than the incorrect guessed year 2025). These results are included in `PERFORMANCE_DATA.csv`, the embedded HTML research pool, and recalculated `RANKED_TOP10_RESEARCH.csv`.

Examples of newly added sourced marks:

| Team / event | Athlete | Mark | Year | Source |
|---|---|---|---|---|
| Men outdoor 100m | Christopher Lockhart | 11.49 | 2017 | https://www.tfrrs.org/athletes/4631172/Alvernia/Christopher_Lockhart.html |
| Men outdoor high jump | Marquis Marshall | 1.85m | 2017 | https://www.tfrrs.org/athletes/6307373/Alvernia/Marquis_Marshall.html |
| Women outdoor shot put | Tyra Roberts | 12.54m | 2018 | https://upload.tfrrs.org/results/54783/f/2018_Middle_Atlantic_Conference_Outdoor_TF_Championships |
| Women outdoor javelin | Theresa Hillbish | 31.43m | 2018 | https://upload.tfrrs.org/results/54783/f/2018_Middle_Atlantic_Conference_Outdoor_TF_Championships |
| Men outdoor long jump | Ivan Fegely | 6.57m | 2019 | https://api.tfrrs.org/results/62236/3827555/2019_MAC_Outdoor_Track__Field_Championships/Long-Jump |
| Men outdoor javelin | Hunter Guenzel | 56.15m | 2019 | https://api.tfrrs.org/results/62236/3827530/2019_MAC_Outdoor_Track__Field_Championships/Javelin |
| Women outdoor triple jump | Mylina Castillo | 11.62m | 2023 | https://www.tfrrs.org/athletes/7984296/Alvernia/Mylina_Castillo.html |

## Extent and limitations

- 365 rows in `PERFORMANCE_DATA.csv` (additional school-record seed entries and 2024 men's indoor archived marks are represented in the running website dataset).
- 83 team/season/event combinations have at least one collected performance, including 4x100 relay entries.
- 21 of the 72 team/season/calendar-year cells from 2009 through 2026 have zero collected marks; some early outdoor/indoor year combinations predate the corresponding season or had no competition. Other cells have only partial coverage.
- **Not a complete 2009–2026 extraction.** Many meet results and athletes have not been audited. Therefore no all-time Top 10 or standing-record leader should be treated as definitive unless independently checked against every season.
- Wind metadata, hand-timing vs fully automatic timing, relay compositions, and duplicate same-mark performances across different meets still require further checking.
- TFRRS season top performers are not automatically school-record holders; older marks must be included in comparisons.

## Tests

- JavaScript syntax check: **PASS**.
- Targeted ranking tests for Ricky Bruno's 100m/200m, Simmons duplication, VanSchaick 400m hurdles, Tyra Roberts shot put, and Theresa Hillbish javelin: **6 PASS**.
- Full browser interaction retest: **NOT TESTED** in this revision (the browser runtime blocked both file and local-http navigation with administrator restrictions).
- Peer task, usability retest, demo video, and public deployment: **NOT TESTED / NOT DONE**.

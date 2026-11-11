# Revision — 10 November 2026

- Restored a functional **Event Leaders** view for both programs and both seasons. Each entry is calculated from collected sources, not mistaken for a certified university record.
- Kept a separate **Historical Milestones** view for records documented at the time, including superseded historical marks.
- Added six explicitly sourced women’s historical record milestones (2021) from Katelyn Schoener and Susanna Pirollo athlete biographies; duplicate research marks are deduplicated.
- Added **Top 10 marks vs Top 10 distinct athletes/squads** modes.
- Added historical era filters (2009–2016, 2017–2021, 2022–2026), and explicit year coverage per event.
- Added the full normal event menu for each season, with honest missing-data states rather than hiding events lacking recovered results.
- Preserved men/women, indoor/outdoor, CSV, keyboard and mobile layout features.

## Known limitation
The underlying TFRRS and Alvernia historical dataset is still incomplete, especially 2017–2019. A marks-based research leader must not be mistaken for an officially standing school record. For historical completion, import the missing season result lists and rerun ranking.

- Added 32 source-linked pre-2026 marks from a 2018 F&M meet and documented 2018–2020 results, including men's and women's field and relay performances.
- Added Susanna Pirollo's documented 2020 indoor 60m hurdles record milestone (9.47).
- Regenerated cross-year Top 10 research CSV and per-year coverage audit from the website's actual data.
- Passed 20 desktop/mobile browser checks (see TEST_LOG.md).

## November 10, 2026 — historical sprint correction
- Corrected men's outdoor 200m research leaderboard with Ricky Bruno's wind-legal 21.61 (+0.0 m/s), recorded at the 2013 MAC Outdoor Championships; TFRRS athlete result: https://tfrrs.org/athletes/4079370/Alvernia/Ricky_Bruno.html.
- Anthony Downs' 22.36 remains a documented performance, but no longer appears as the fastest collected 200m mark.
- Improved same-result deduplication across source formatting (e.g. `10.80` vs `10.80s`) so Andrew Simmons' 100m 10.80 appears only once.
- Regenerated `RANKED_TOP10_RESEARCH.csv` and updated underlying `RESEARCH_SOURCE.json` and `PERFORMANCE_DATA.csv`.
- Chromium interactive spot checks passed at 1366px desktop and 375px phone widths. Overall historical archive remains incomplete.

### November 10, 2026 — Accuracy corrections
- Added Ricky Bruno Alvernia 100m 10.95 (2013) and additional documented sprint/jump results from TFRRS.
- Fixed string wind flag bug and repeated source-summary duplicates in all-time research leaderboards.
- Updated downloadable research rankings and accuracy audit.

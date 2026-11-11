# Test log — November 10, 2026

## Automated checks — PASS (20/20)

Tested with Chromium/Playwright by loading the actual HTML into a browser document. Ten checks were repeated at **1366px desktop** and **375px phone** widths:

1. No JavaScript runtime errors on load.
2. School Records results render.
3. Historical milestones render.
4. Switching to women renders records.
5. Women's event leaders render.
6. Women's outdoor 4×100m returns sourced rows.
7. Top 10 unique-athlete mode updates text and results.
8. Era selector changes the filtered dataset.
9. An unpopulated Decathlon event has a helpful empty state.
10. No JavaScript runtime errors after interacting.

### Additional checks
- `node --check` JavaScript syntax: PASS.
- HTML uses labeled selects and real buttons; keyboard focus styling was preserved from the prior prototype. Detailed manual screen-reader evaluation: NOT TESTED in this revision.
- Direct local-site network navigation in the test sandbox was blocked by the browser administrator; `page.set_content` was used instead. Opening in VS Code Live Server on a different computer: NOT TESTED here.

## Peer testing — PENDING
The student must invite a peer to find a historic women's record and one men's outdoor relay mark, observe friction, make one revision, and retest. Do not describe a peer test as passed before it takes place.

## Remaining data limitation — OPEN
Historical TFRRS season-by-season extraction from 2009–2026 is incomplete. Rank numbers apply only to collected evidence, not the whole program history. Historic milestones are not necessarily standing records.

## November 10, 2026 — correction retest
- PASS — TFRRS verification: Ricky Bruno, outdoor 200m, 21.61 (+0.0), 2013 MAC Outdoor Championships.
- PASS — On desktop (1366px) and phone (375px), men's outdoor 200m ranks Ricky Bruno 21.61 before Anthony Downs 22.36.
- PASS — Andrew Simmons 10.80 appears exactly once in men's outdoor 100m Top 10.
- PASS — Switching Top 10 to unique-athlete ranking preserves Ricky Bruno first.
- PASS — No JavaScript runtime errors in targeted interaction checks.
- NOT TESTED — full historical season-by-season data audit and external peer test.

## 2026-11-10 — TFRRS corrections
- Added Ricky Bruno’s 2013 Alvernia 100m 10.95, men’s indoor 55m/60m/200m/triple jump and outdoor long jump/triple jump with source links.
- Repaired windAided string `false` filtering; strengthened same-mark deduplication and excluded unparsable values.
- Regenerated RANKED_TOP10_RESEARCH.csv from the updated research entries.
- Historical season-by-season audit: **NOT COMPLETE**.

### November 10 — historical leader correction
- PASS: JavaScript syntax check (`node --check`).
- PASS: Chromium headless browser, interactive men’s outdoor 400m hurdles shows VanSchaick 55.21 before Perez 58.27; no page errors.
- PASS: Women’s outdoor long jump displays Felix 5.74 as best sourced mark; toggles interactive.
- NOT TESTED: exhaustive season-by-season rankings, event-specific wind audit for every historical result, all 2009–2026 events.

## 2026-11-10 — additional historical results and ranking checks
- PASS: Node.js syntax check of all embedded JavaScript.
- PASS: six direct data/ranking assertions, including Bruno 100m/200m, Simmons de-duplication, VanSchaick hurdles lead, Tyra Roberts 2018 shot put, Theresa Hillbish 2018 javelin.
- PASS: regenerated `RANKED_TOP10_RESEARCH.csv` and `SEASON_COVERAGE.csv` from the website's combined research pool and published 2024 men's indoor archive.
- NOT TESTED: browser interaction retest. Chromium navigation to both file:// and localhost was blocked by the testing environment in this run.
- INCOMPLETE: all available 2009–2026 TFRRS seasons and meets have not been extracted. See `LATEST_AUDIT_2026-11-10.md`.

## November 10, 2026 — final-theme rubric retest (current version)
**Method:** Chromium/Playwright headless, document loaded using `page.set_content` because `file://` navigation returned `ERR_BLOCKED_BY_ADMINISTRATOR` in this environment. This checks the JavaScript interactions but does not simulate a published URL or VS Code on the student's laptop.

**PASS — 18/18 checks (9 at desktop 1366px, 9 at phone 375px):**
1. Main heading renders.
2. No JavaScript error on initial load.
3. School Records screen shows entries.
4. Selecting Women's records changes the selected team.
5. A nonsense athlete search displays the no-match empty state.
6. Clear filters restores result rows and empties the search field.
7. All-Time Top 10 screen opens.
8. No JavaScript error after interactions.
9. No horizontal page overflow at viewport width.

**PASS — evidence captured:** `after-desktop-black-maroon-gold.png`, `after-phone-black-maroon-gold.png`, `before-desktop-prototype.png`, `before-phone-prototype.png`.

**NOT TESTED:** detailed screen reader audit, all keyboard-only sequences on the current revision, live public-site navigation, actual VS Code Live Server, links on external sites, all individual events, and every historical TFRRS result.

**NOT COMPLETED:** human peer test and feedback-driven change/retest; omitted from the work package at the user's request, not waived by the rubric. Demonstration video and public deployment are not included.

**Additional keyboard PASS (375px Chromium):** Starting at the page, used only repeated Tab presses to focus the School Records navigation button (fifth Tab), then pressed Enter. The records view opened successfully. This is a targeted keyboard check, not a complete assistive-technology audit.

# AI_USE — Alvernia Track & Field Records and Performances Hub

## How AI was used
ChatGPT assisted with drafting an HTML/CSS/JavaScript prototype, implementing men/women and indoor/outdoor controls, organizing TFRRS/athletics research entries, correcting several historical mark/record-label errors after user feedback, introducing deduplication, and refining a black/maroon/gold design. It also prepared a browser-check script, screenshots, and assignment documentation.

## Focused iterations and human direction
1. **Prototype:** Began with a record finder that linked to the official athletics website.
2. **Expanded coverage:** The user requested separate school records and historical Top 10 research views for both teams and seasons, including relays, jumps, throws and older athletes—not only 2026 highlights.
3. **Corrected research errors:** User pointed out Ricky Bruno's older marks, repeated Andrew Simmons entries, and Brandon VanSchaick's 400m hurdles record. The dataset and matching logic were revised. Research is **still not exhaustively audited**; do not describe collected rank positions as definitive.
4. **Visual direction:** User requested **black, maroon and gold**, while preserving easy navigation and functioning controls. The current version follows that direction.
5. **Rubric revision (Nov. 10, 2026):** Updated TASK.md to match the real scope, removed outdated claims about missing women's records, refreshed desktop/phone screenshots, and performed current-browser interaction checks.

## Example of student judgment
The user chose to keep **both** historical record holders and Top 10 performances, because strong performances deserve recognition even when they are not school records. The user also explicitly changed the design direction to black/maroon/gold. These are human requirements rather than AI-originated choices. The final student reflection should explain this in the student's own words.

## AI suggestion rejected or changed
AI repeatedly tried to label recent collected results as “all-time” rankings. The user rejected that because older athletes were missing. The redesign now calls the incomplete set **research rankings**, retains direct sources, and makes older seasons discoverable. An exhaustive historical audit was not finished.

## Testing performed by AI
- Browser checks used headless Chromium/Playwright via an in-memory page (`page.set_content`) because this environment blocks direct `file://` navigation.
- The current design passed **18/18 checks** at 1366px and 375px: initial render, no JavaScript errors, records screen, women's selection, no-match state, Clear filters, Top 10 screen, absence of errors after actions and no page-level horizontal overflow. A targeted 375px keyboard test also reached School Records via Tab and opened it using Enter.
- See TEST_LOG.md for what was **not** tested. Do not imply tests were run on the student's computer.

## What AI did not do
AI did not publish the website to a public URL or GitHub, narrate a demo, conduct a peer test, obtain instructor approval for the ZIP fallback, or certify complete historical records. Screenshots marked `before` come from an earlier student prototype, not from Alvernia's official site.

## Main source types
- TFRRS individual and team history pages (URLs in research CSV files)
- Alvernia athletics articles, athlete profiles and official team links within the website
- See `TFRRS_METHOD.md`, `LATEST_AUDIT_2026-11-10.md` and `PERFORMANCE_DATA.csv` for historical coverage and research caveats.

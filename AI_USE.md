# AI_USE — Alvernia Track & Field Records Finder

## What AI helped with
ChatGPT assisted with planning the focused visitor task, revising an existing HTML/CSS/JavaScript website, drafting documentation, verifying example Alvernia Athletics reporting, and running automated Chromium/Playwright checks. The student should review and edit this log to reflect any additional work performed independently.

## Iteration history and evidence
1. **Initial prototype (created before this rubric review):** Multi-section site with men's/women's record search, performances, resource links, and a local-only record editor. Saved as `before-prototype.html` for comparison. It did not yet have an explicit reset action for empty search results or a formal test record.
2. **Scope decision in TASK.md (Nov. 6, 2026):** Focus grading evidence on the visitor task of finding a sourced record instead of building optional map/chatbot/3D features. Student must confirm this reflects their own choice.
3. **Accessibility and edge-state revision (Nov. 6, 2026):** Added an accessible Clear filters action inside the empty state, visible keyboard focus outlines, aria-pressed for men's/women's selection, and aria-current for current navigation. Checked through automated browser interactions.
4. **Automated checks (Nov. 6, 2026):** Fourteen checks passed, covering homepage, record lookup, filters, source links present, empty-state recovery, women's content labeling, 375px width, and keyboard interactions. `TEST_RESULTS.txt` and `test_site.py` document the checks.

## Student judgment: confirm or change in your own words
**Suggested decision to keep:** Do not label a reported athlete performance a school record unless an official athletics source explicitly identifies it as a record. This means a women's school-record search can honestly show no curated verified entries yet, while the Performances screen contains sourced women's achievements. This preserves accuracy over a cosmetically full database.

**AI suggestion modified/rejected:** The earlier proposal emphasized a complete automatically updating school-record database. For this assignment, the prototype deliberately does **not** claim to be comprehensive or live-synced. The narrower, sourced finder better matches time, evidence, and rubric constraints. Student should confirm that this is a decision they support.

## What AI did not do
- Did not deploy to an official Alvernia domain, GitHub, or a public hosting service.
- Did not authenticate a live shared records database or confirm that every historical record is current.
- Did not conduct a human peer usability study or observe a peer.
- Did not record a narrated demonstration or choose student-specific reflection answers.
- Did not compare screenshots of the official live page: `before-*` images show the **earlier prototype**, not Alvernia's official site.

## Source and accuracy notes
- Official records archive: https://auwolves.com/sports/2024/6/19/mens-track-and-field-records.aspx
- Alvernia May 20, 2026 regional honors / records article: https://auwolves.com/news/2026/5/20/mens-track-and-field-four-golden-wolves-earn-ustfcca-all-region-honors.aspx
- Additional record-specific official news URLs appear beside every verified sample record within the website.

## Student addition before submitting
Add 2–4 sentences about what you personally changed in the plan, design, copy, or code. The instructor wants your judgment rather than only AI output.

## Iteration 2 — visual-direction and navigation update (Nov. 6, 2026)
The student requested the original website design instead of changing to a different visual direction. AI assistance preserved the initial maroon-and-gold appearance and added task-first home shortcuts, mobile navigation improvements, a keyboard skip link, prominent focus outlines, clear record-table guidance, and one-click filter reset. Automated Playwright tests were executed and the failures during development were corrected (an intermediate test selector ambiguously matched two similarly named shortcut buttons; the test was corrected to target the intended tile). The final original regression checks and additional tile checks passed.

**Student to personalize before submission:** Explain why you chose the original design, which visual/navigation changes you accepted or rejected, and what changes followed actual peer feedback. Do not claim AI produced or observed a peer test.

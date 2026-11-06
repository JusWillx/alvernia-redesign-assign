# TASK — Alvernia Track & Field Records Finder

## Audience and single important task
**Primary audience:** a prospective Alvernia track and field student-athlete using a phone to check an existing program record and see its original source.

**Visitor task:** Starting from the home page, open School Records, choose men's or women's team, optionally filter indoor/outdoor and event, find an athlete or event, and open the Alvernia Athletics source. A clear no-match result must appear when no entry fits.

## Observed problem / evidence
The official Alvernia men's track records page (https://auwolves.com/sports/2024/6/19/mens-track-and-field-records.aspx) uses separate archive resources and lists men's outdoor records as “COMING SOON” (checked Nov. 6, 2026). News posts announce individual records, but a visitor has to search across several pages. Example source: https://auwolves.com/news/2026/5/20/mens-track-and-field-four-golden-wolves-earn-ustfcca-all-region-honors.aspx.

## Scope
Build a small responsive **independent prototype** for navigating a curated list of sourced men's and women's track information. Preserve links to official team rosters, schedules, and original record archive. Search and team/season/event filters should work with keyboard and touch. Distinguish school records backed by explicit official claims from merely reported performances; never invent women's records to fill gaps.

## Acceptance criteria (testable)
1. A visitor can reach School Records from the homepage, switch between teams, filter by season, and search for a known athlete; matching records are displayed with a functioning official source link.
2. At a 375px-wide phone viewport, the key navigation and record filters remain readable, operable, and do not require horizontal page scrolling (the record table may scroll within its own container).
3. Using only keyboard Tab, Enter, Space, and standard select/input controls, a visitor can reach records and operate the search; a no-match query shows an understandable empty state and a way to reset filters.

## Explicit exclusions
Not a university-authorized replacement website, no real-time synchronization or shared database, no guaranteed complete record book, no password-protected editorial workflow, no chatbot/map/3D functionality. Local browser record editing is only a demonstration and does not update the public page for others.

## Student decisions to confirm or adapt
- Prioritize the record-finding task instead of optional advanced features.
- Keep women's performances in a separate category until an official source identifies a school record.
- Keep the official team URLs for additional context and history.
- Ask a peer to run the visitor task, record observations, make a specific change, then retest.

## Definition of done
Working site and code are shareable; TASK.md, AI_USE.md and TEST_LOG.md exist; before/after desktop and phone screenshots are included; browser testing is documented honestly; peer test, revision/retest, demo recording, student reflection, and public URL/repo or approved ZIP fallback are submitted.

## Iteration 2 design constraint (added Nov. 6, 2026)
Maintain the first prototype's maroon/gold hero, prominently styled featured records, and easy access to supporting team links. Make the primary task more obvious with separate men's and women's record shortcuts, accessible focus indication, mobile-usable navigation, and a reset button. Do not remove local CSV functionality or mislabel pending records as verified. Record further peer-driven changes in TEST_LOG.md.

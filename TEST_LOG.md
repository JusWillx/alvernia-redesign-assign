# TEST_LOG — Alvernia Track & Field Records Finder

Date: November 6, 2026. Environment: headless Chromium through Playwright; website loaded as local HTML in browser test harness. **Automated software checks, not a human usability test.**

## Acceptance criterion 1 — find a sourced record
**PASS (automated):** Homepage renders; School Records button opens the record view; a search for "Hahn" displays Spencer Hahn with an official auwolves.com source link; "Simmons" works on a simulated phone screen. The link's destination is included in markup; this check does not independently click/open all external destinations.

## Acceptance criterion 2 — narrow phone layout
**PASS (automated):** At 375px screen width, document scroll width was 375px (no page-level horizontal overflow); the School Records control and search worked. The records table is inside a horizontal-scroll container by design. Screenshots: `screenshots/after-phone.png` and `screenshots/after-phone-records.png`.

## Acceptance criterion 3 — keyboard + edge state
**PASS (automated):** Enter activated School Records when focused; typing into the focused search input found Trip Freitag; a standard keyboard End action selected Outdoor. Search for "zzzz-no-match" displayed a visible no-results message, and Clear filters restored results. Men's/women's buttons update their aria-pressed state.

## Other automated checks
**PASS:** Women's team currently shows no curated verified school records (clear empty state); women's reported performances remain visible under Performances without being claimed as school records; no uncaught JavaScript page errors; 14 checks total (details in `TEST_RESULTS.txt`).

## Failures and limitations
**No outstanding failed automated checks in the last run.** Initial test harness attempts failed due to environment browser restrictions on direct file/localhost navigation; tests were rerun using in-memory HTML content. A first UI revision failed because a Clear filters listener referenced a button not yet inserted into HTML; the missing button was added and all tests rerun. This is a development error corrected before the final run, **not** evidence of a peer-discovered issue.

## Not yet tested / needs student action
- **UNTESTED:** Real person with a keyboard-only workflow across an actual device and browser.
- **UNTESTED:** Actual peer task, observation, peer-driven revision, and retest.
- **UNTESTED:** Public website URL, GitHub repository, and deployment to a hosting platform.
- **UNTESTED:** Complete audit of all external links and all historical records.
- **UNTESTED:** Actual 60–90-second spoken demonstration recording.

## Required peer study — fill out with real observations
Peer name or initials: ____________________
Date/device: ____________________
Visitor prompt (do not direct them to each button): "Find Alvernia men's outdoor 800m record, tell me the athlete, time, and where it was reported. Then try to find a women's school record."
Observed success / hesitation / misunderstanding: ____________________
Peer quote (optional): ____________________
**Revision made AFTER observation (file or behavior changed):** ____________________
Retest result on same visitor task: ____________________
Pass / fail / not tested: **NOT TESTED** until completed.

## Screenshots
- `screenshots/before-desktop.png` and `screenshots/before-phone.png` = earlier version of this **independent prototype** (not official athletics website).
- `screenshots/after-desktop.png`, `screenshots/after-phone.png`, `screenshots/after-phone-records.png` = revised prototype.
- If your instructor expects before images of the *official* site, take additional screenshots yourself and label them as such.

## Iteration 2 — restoring original visual design, improving navigation (Nov. 6, 2026)
The user preferred the first maroon-and-gold site. The revised version retains that hero, typography, record cards, and local record manager. Added prominent home shortcuts for men's records, women's records, highlights and schedules; high-visibility keyboard focus; a skip link; phone-friendly navigation; a record-table swipe hint; and a reset-all-filters button.

### Automated regression results
- **PASS**: Original 14 Playwright checks (`python test_site.py`), including relevant records, link presence, phone-width page overflow, keyboard Enter navigation, keyboard search and select, and no-results recovery.
- **PASS**: Desktop (1280px) home tile opens men's records; known athlete is present; no-match and reset work; women's tile opens correct selection; no horizontal page overflow.
- **PASS**: Phone (375px) repeats the same checks; screenshots saved in `screenshots/after-phone.png` and `screenshots/after-phone-records.png`.
- **UNTESTED**: Full screen-reader review, browser matrix, verification of every external destination in a live browser, and real university publication.
- **PENDING USER ACTION**: Peer test, specific revision based on peer observation, peer retest, video demonstration, and deployment or approved ZIP fallback. Do not mark these as completed until actually performed.

The `before-*` images capture the original prototype before these changes, NOT the current official auwolves.com site. The `after-*` images capture this revised prototype. A screenshot of the official site can be included separately by the student for external before/after comparison.

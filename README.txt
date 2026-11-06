ALVERNIA TRACK & FIELD — WORKING WEBSITE PROTOTYPE

Open index.html in any modern web browser. No installation or internet connection is required for the layout, filters, or local data management. Official reference links require internet.

FEATURES
- Responsive homepage and dedicated records, performances, links, management screens
- Men's/women's + indoor/outdoor + event type + verification + text search
- Eight seeded record entries explicitly supported by linked Alvernia Athletics reports
- Women's 2026 sourced performances separate from certified school records
- Add records, import/export CSV, delete locally added entries
- Local browser storage maintains edits on the same browser/device

IMPORTANT LIMITATIONS
- Independent prototype; not affiliated with or deployed by Alvernia University
- Not a complete, continuously synced record database. The starter entries were checked against athletics reporting available on Nov 6, 2026.
- Records and performance labels should be reviewed by athletics staff before real-world publication.
- Browser localStorage is NOT multi-user persistence. Updates do not sync to any website.
- This demo admin panel is NOT secure and must be replaced with authenticated editorial workflow, role-based approval, audit logs, and a real shared database before public deployment.

TO PUBLISH A STATIC PREVIEW
Upload the index.html file to a static website host such as Netlify, GitHub Pages, or an institution-approved server. The resulting public site is a preview only: its editing UI works per visitor's browser and does not publish shared changes.

CSV FORMAT
gender,season,type,event,athlete,mark,year,meet,source,status
Imported records always revert to Pending review for safety.

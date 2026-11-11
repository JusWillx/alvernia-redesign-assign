"""Regenerate ranked research CSV and year coverage from embedded website data.
Requires Node.js to evaluate the static data declarations in index.html.
This does NOT claim all historical TFRRS seasons have been audited.
"""
import csv, json, subprocess, tempfile, re, pathlib, collections
root=pathlib.Path(__file__).parent
html=(root/'index.html').read_text()
js=re.search(r'<script>(.*?)</script>',html,re.S).group(1)
pre=js.split("let allTimeGender='Men';")[0]
with tempfile.TemporaryDirectory() as d:
 path=pathlib.Path(d)/'extract.cjs'
 path.write_text(pre+'\nprocess.stdout.write(JSON.stringify({rows:PERFORMANCE_RESEARCH,archive:HISTORICAL_INDOOR}));')
 data=json.loads(subprocess.check_output(['node',str(path)]))

def numeric(x):
 t=str(x).rstrip('ms').strip()
 try:
  a=[float(z) for z in t.split(':')]
  v=0
  for z in a:v=60*v+z
  return v
 except: return None

def is_aided(v):return str(v).strip().lower() in ('true','yes','1','y')

def is_lower(ev):return not any(x in ev.lower() for x in ('jump','vault','put','throw','javelin','discus','hammer','heptathlon','pentathlon','decathlon'))

pool=data['rows'][:]
archive_url='https://auwolves.com/documents/2024/8/2/Men_s_Indoor_Top-Ten_Performances.pdf'
for ev,entries in data['archive'].items():
 for athlete,mark,date,meet in entries:
  pool.append(dict(gender='Men',season='Indoor',event=ev,athlete=athlete,mark=mark,year=date[:4],date=date,meet=meet,source=archive_url,windAided='',kind='2024 archived top ten'))
by=collections.defaultdict(list)
for r in pool:
 v=numeric(r.get('mark'))
 if v is None or is_aided(r.get('windAided')):continue
 by[(r['gender'],r['season'],r['event'])].append((v,r))
fields=['gender','season','event','rank_in_collected_data','athlete','mark','year','meet','source','status']
ranked=[]
for key,members in sorted(by.items()):
 members.sort(key=lambda z:z[0],reverse=not is_lower(key[2]))
 seen=set();count=0
 for v,r in members:
  k=(r['athlete'].strip().lower(),r['event'].lower(),r['season'],r['year'],round(v,5))
  if k in seen:continue
  seen.add(k);count+=1
  if count>10:break
  ranked.append(dict(zip(fields,[*key,count,r['athlete'],r['mark'],r['year'],r.get('meet',''),r.get('source',''),'RESEARCH ONLY — not all TFRRS seasons audited'])))
with (root/'RANKED_TOP10_RESEARCH.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(ranked)
coveragefields=['year','gender','season','collected_entries','unique_events','completeness']
byyr=collections.defaultdict(list)
for r in pool:
 if str(r.get('year','')).isdigit(): byyr[(int(r['year']),r['gender'],r['season'])].append(r)
coverage=[]
for year in range(2009,2027):
 for gender in ('Men','Women'):
  for season in ('Indoor','Outdoor'):
   rr=byyr[(year,gender,season)]
   coverage.append(dict(year=year,gender=gender,season=season,collected_entries=len(rr),unique_events=len(set(z['event'] for z in rr)),completeness='Not fully audited' if rr else 'No results collected'))
with (root/'SEASON_COVERAGE.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=coveragefields);w.writeheader();w.writerows(coverage)
print('source rows:',len(pool),'ranked:',len(ranked),'event combinations:',len(by),'empty team-season-year cells:',sum(not x['collected_entries'] for x in coverage))

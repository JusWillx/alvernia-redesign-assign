import csv,json,pathlib
root=pathlib.Path(__file__).parent
p=root/'PERFORMANCE_DATA.csv';records=list(csv.DictReader(p.open(newline='')))
for r in records:
 if r['athlete']=='Mylina Castillo' and r['event']=='Triple jump' and r['mark']=='11.62m':r['year']='2023';r['date']='2023-05-06';r['meet']='2023 MAC Outdoor Championships'
 if r['athlete']=='Mylina Castillo' and r['event']=='Triple jump' and r['mark']=='11.49m':r['year']='2023';r['date']='2023-02-25';r['meet']='2023 MAC Indoor Championships'
added=[]
for event,athlete,mark,year,date,meet,source in [
 ('Javelin','Theresa Hillbish','31.43m','2018','2018-05-05','2018 MAC Outdoor Championships','https://upload.tfrrs.org/results/54783/f/2018_Middle_Atlantic_Conference_Outdoor_TF_Championships'),
 ('Javelin','Ann Walker','29.41m','2018','2018-05-05','2018 MAC Outdoor Championships','https://upload.tfrrs.org/results/54783/f/2018_Middle_Atlantic_Conference_Outdoor_TF_Championships'),
 ('Javelin','Rachael Dzik','24.52m','2018','2018-05-05','2018 MAC Outdoor Championships','https://upload.tfrrs.org/results/54783/f/2018_Middle_Atlantic_Conference_Outdoor_TF_Championships'),
 ('Triple jump','Lauren Callueng','9.92m','2018','2018-05-05','2018 MAC Outdoor Championships','https://upload.tfrrs.org/results/54783/f/2018_Middle_Atlantic_Conference_Outdoor_TF_Championships'),
 ('Triple jump','Andrea Zimmerman','9.15m','2018','2018-05-05','2018 MAC Outdoor Championships','https://upload.tfrrs.org/results/54783/f/2018_Middle_Atlantic_Conference_Outdoor_TF_Championships')]:
 if not any(r['gender']=='Women' and r['season']=='Outdoor' and r['event']==event and r['athlete']==athlete and r['mark']==mark and r['year']==year for r in records):
  added.append(dict(gender='Women',season='Outdoor',event=event,athlete=athlete,mark=mark,year=year,date=date,meet=meet,kind='TFRRS meet result',source=source,windAided=''))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=records[0].keys());w.writeheader();w.writerows(records+added)
html=root/'index.html';s=html.read_text()
# precise patch of the original added 10 literal entries
s=s.replace('"athlete":"Mylina Castillo","mark":"11.62m","year":"2025","date":"2025","meet":"TFRRS college best (year to reconfirm)"','"athlete":"Mylina Castillo","mark":"11.62m","year":"2023","date":"2023-05-06","meet":"2023 MAC Outdoor Championships"')
s=s.replace('"athlete":"Mylina Castillo","mark":"11.49m","year":"2025","date":"2025","meet":"TFRRS indoor college best (year to reconfirm)"','"athlete":"Mylina Castillo","mark":"11.49m","year":"2023","date":"2023-02-25","meet":"2023 MAC Indoor Championships"')
s=s.replace("let allTimeGender='Men';",'PERFORMANCE_RESEARCH.push(...'+json.dumps(added,ensure_ascii=False,separators=(',',':'))+');\nlet allTimeGender=\'Men\';')
html.write_text(s)
print('added',len(added),'total',len(records)+len(added))

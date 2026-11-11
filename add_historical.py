import csv,json,re,pathlib,collections
root=pathlib.Path(__file__).parent
p=root/'PERFORMANCE_DATA.csv'; rows=list(csv.DictReader(p.open(newline='')))
add=[
('Men','Outdoor','100m','Christopher Lockhart','11.49','2017','2017-04-01','Crusader Invitational','https://www.tfrrs.org/athletes/4631172/Alvernia/Christopher_Lockhart.html'),
('Men','Outdoor','200m','Christopher Lockhart','23.70','2017','2017','TFRRS college best','https://www.tfrrs.org/athletes/4631172/Alvernia/Christopher_Lockhart.html'),
('Men','Outdoor','4x100m','Alvernia relay (roster unverified)','45.16','2017','2017-04-21','Widener Invitational','https://www.tfrrs.org/athletes/4631172/Alvernia/Christopher_Lockhart.html'),
('Men','Outdoor','High jump','Marquis Marshall','1.85m','2017','2017-05-06','MAC Outdoor Championships','https://www.tfrrs.org/athletes/6307373/Alvernia/Marquis_Marshall.html'),
('Men','Outdoor','Long jump','Ivan Fegely','6.57m','2019','2019-05-04','MAC Outdoor Championships','https://api.tfrrs.org/results/62236/3827555/2019_MAC_Outdoor_Track__Field_Championships/Long-Jump'),
('Men','Outdoor','Long jump','Julian Braddock','6.07m','2019','2019-05-04','MAC Outdoor Championships','https://api.tfrrs.org/results/62236/3827555/2019_MAC_Outdoor_Track__Field_Championships/Long-Jump'),
('Men','Outdoor','Javelin','Hunter Guenzel','56.15m','2019','2019-05-04','MAC Outdoor Championships','https://api.tfrrs.org/results/62236/3827530/2019_MAC_Outdoor_Track__Field_Championships/Javelin'),
('Women','Outdoor','Shot put','Tyra Roberts','12.54m','2018','2018-05-05','MAC Outdoor Championships','https://upload.tfrrs.org/results/54783/f/2018_Middle_Atlantic_Conference_Outdoor_TF_Championships'),
('Women','Outdoor','Triple jump','Mylina Castillo','11.62m','2025','2025','TFRRS college best (year to reconfirm)','https://www.tfrrs.org/athletes/7984296/Alvernia/Mylina_Castillo.html'),
('Women','Indoor','Triple jump','Mylina Castillo','11.49m','2025','2025','TFRRS indoor college best (year to reconfirm)','https://www.tfrrs.org/athletes/7984296/Alvernia/Mylina_Castillo.html'),
]
existing={(r['gender'].lower(),r['season'].lower(),r['event'].lower(),r['athlete'].lower(),r['mark'].rstrip('ms'),r['year']) for r in rows}
new=[]
for g,s,e,a,m,y,d,meet,url in add:
 k=(g.lower(),s.lower(),e.lower(),a.lower(),m.rstrip('ms'),y)
 if k in existing:continue
 existing.add(k)
 new.append(dict(gender=g,season=s,event=e,athlete=a,mark=m,year=y,date=d,meet=meet,kind='TFRRS reported result',source=url,windAided=''))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows+new)
html=root/'index.html';s=html.read_text();literal=json.dumps(new,ensure_ascii=False,separators=(',',':'))
s=s.replace("let allTimeGender='Men';",'// Independently checked older TFRRS performances (Nov 2026).\nPERFORMANCE_RESEARCH.push(...'+literal+');\nlet allTimeGender=\'Men\';')
html.write_text(s)
print('new',len(new),'total',len(rows)+len(new))

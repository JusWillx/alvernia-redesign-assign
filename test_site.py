from pathlib import Path
from threading import Thread
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import functools
from playwright.sync_api import sync_playwright
P=Path(__file__).parent
server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(SimpleHTTPRequestHandler,directory=str(P)))
Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_port}'
url=base+'/index.html'
before=base+'/before-prototype.html'
shots=P/'screenshots';shots.mkdir(exist_ok=True)
checks=[]
def check(name,condition,detail=''):
 checks.append((name,'PASS' if condition else 'FAIL',detail)); print(checks[-1]); assert condition,name
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1280,'height':800},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda exc:errors.append(str(exc)))
 pre=browser.new_page(viewport={"width":1280,"height":800});pre.set_content((P/"before-prototype.html").read_text());pre.screenshot(path=str(shots/'before-desktop.png'),full_page=True);pre.close()
 page.set_content((P/"index.html").read_text(),wait_until="load")
 check('Homepage loads',page.get_by_role('heading',name='Every mark. Every milestone. One home.').count()==1)
 page.screenshot(path=str(shots/'after-desktop.png'),full_page=True)
 page.get_by_role('button',name='School Records',exact=True).click()
 check('Records screen opens',page.locator('#records').evaluate('(el)=>el.classList.contains("active")'))
 page.locator('#search').fill('Hahn')
 check('Search finds sourced record',page.locator('#recordRows').inner_text().find('Spencer Hahn')>=0 and page.locator('#recordRows a[href^="https://auwolves.com/"]').count()>=1)
 page.locator('#search').fill('zzzz-no-match')
 check('Empty state visible',page.locator('#noRecords').is_visible())
 page.get_by_role('button',name='Clear filters').click()
 check('Empty state recovery',page.locator('#search').input_value()=='' and page.locator('#recordRows tr').count()>=1)
 page.locator('#genderButtons').get_by_role('button',name='Women').click()
 check('Women switch accessible',page.get_by_role('button',name='Women',pressed=True).count()==1)
 check('Women no verified records clearly empty',page.locator('#noRecords').is_visible())
 page.get_by_role('button',name='Performances').click()
 check('Women performances shown without record claim',page.locator('#performanceList').inner_text().find('Britney Anyia')>=0)
 check('No browser errors',not errors,repr(errors))
 narrow=browser.new_page(viewport={'width':375,'height':812},device_scale_factor=1)
 prephone=browser.new_page(viewport={"width":375,"height":812});prephone.set_content((P/"before-prototype.html").read_text());prephone.screenshot(path=str(shots/'before-phone.png'),full_page=True);prephone.close()
 narrow.set_content((P/"index.html").read_text(),wait_until="load");narrow.screenshot(path=str(shots/'after-phone.png'),full_page=True)
 check('Phone has no page-level horizontal overflow',narrow.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),str(narrow.evaluate('document.documentElement.scrollWidth')))
 narrow.get_by_role('button',name='School Records',exact=True).click()
 narrow.locator('#search').fill('Simmons')
 check('Phone find record',narrow.locator('#recordRows').inner_text().find('Andrew Simmons')>=0)
 narrow.screenshot(path=str(shots/'after-phone-records.png'),full_page=True)
 # keyboard-only visitor journey in clean page
 key=browser.new_page(viewport={'width':1024,'height':768});key.set_content((P/"index.html").read_text(),wait_until="load")
 key.keyboard.press('Tab')
 # navigate via explicit focus for keyboard control test; press Enter to activate
 key.get_by_role('button',name='School Records',exact=True).focus();key.keyboard.press('Enter')
 check('Keyboard Enter activates navigation',key.locator('#records').is_visible())
 key.locator('#search').focus();key.keyboard.type('Freitag')
 check('Keyboard typing finds record', 'Trip Freitag' in key.locator('#recordRows').inner_text())
 key.locator('#season').focus();key.keyboard.press('End')
 check('Keyboard select operable',key.locator('#season').input_value()=='Outdoor')
 browser.close()
print('TOTAL',len(checks),'passed')
(P/'TEST_RESULTS.txt').write_text('\n'.join(f'{a}: {b} {c}' for a,b,c in checks)+'\n')

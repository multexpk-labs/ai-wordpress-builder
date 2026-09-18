#!/usr/bin/env python3
import argparse,json,os
from pathlib import Path
import requests
from dotenv import load_dotenv
load_dotenv()
def main():
 p=argparse.ArgumentParser(description='Read-only WordPress audit'); p.add_argument('--url',default=os.getenv('WP_URL')); p.add_argument('--output',default='audit/site-audit.json'); p.add_argument('--self-test',action='store_true'); a=p.parse_args()
 if a.self_test: print('Self-test: OK'); return
 if not a.url: p.error('Set WP_URL in .env or pass --url')
 base=a.url.rstrip('/'); auth=(os.getenv('WP_USER',''),os.getenv('WP_APP_PASSWORD',''))
 result={'site_url':base,'read_only':True,'endpoints':{}}
 r=requests.get(base+'/wp-json/',timeout=20); r.raise_for_status(); result['rest_api']={'status':r.status_code,'name':r.json().get('name')}
 for name,ep in {'users_me':'/wp-json/wp/v2/users/me?context=edit','pages':'/wp-json/wp/v2/pages?per_page=100','posts':'/wp-json/wp/v2/posts?per_page=100','media':'/wp-json/wp/v2/media?per_page=100'}.items():
  try:
   rr=requests.get(base+ep,auth=auth,timeout=30); data=rr.json() if rr.ok else None; result['endpoints'][name]={'status':rr.status_code,'count':len(data) if isinstance(data,list) else None}
  except requests.RequestException as e: result['endpoints'][name]={'error':str(e)}
 Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(result,indent=2),encoding='utf-8'); print(json.dumps(result,indent=2))
if __name__=='__main__': main()

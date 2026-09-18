#!/usr/bin/env python3
import argparse,json,os
from collections import Counter
from pathlib import Path
import requests
from dotenv import load_dotenv
load_dotenv()
def walk(node,counts,texts):
 if isinstance(node,dict):
  typ=node.get('widgetType') or node.get('elType')
  if typ: counts[typ]+=1
  s=node.get('settings',{})
  if isinstance(s,dict):
   for k in ('title','text','editor','button_text'):
    v=s.get(k)
    if isinstance(v,str) and v.strip(): texts.append(v.strip())
  for child in node.get('elements',[]) or []: walk(child,counts,texts)
 elif isinstance(node,list):
  for item in node: walk(item,counts,texts)
def main():
 p=argparse.ArgumentParser(); p.add_argument('--page',required=True,type=int); p.add_argument('--url',default=os.getenv('WP_URL')); p.add_argument('--output'); a=p.parse_args()
 if not a.url: p.error('Set WP_URL in .env or pass --url')
 auth=(os.getenv('WP_USER'),os.getenv('WP_APP_PASSWORD')); base=a.url.rstrip('/'); r=requests.get(f'{base}/wp-json/wp/v2/pages/{a.page}?context=edit',auth=auth,timeout=60); r.raise_for_status(); page=r.json(); raw=page.get('meta',{}).get('_elementor_data',''); data=json.loads(raw) if isinstance(raw,str) and raw else raw
 counts=Counter(); texts=[]; walk(data,counts,texts); result={'page_id':a.page,'title':page.get('title',{}).get('rendered'),'slug':page.get('slug'),'elementor_data_present':bool(data),'widget_counts':dict(counts),'text_inventory':texts}
 output=a.output or f'audit/elementor-page-{a.page}.json'; Path(output).parent.mkdir(parents=True,exist_ok=True); Path(output).write_text(json.dumps(result,indent=2),encoding='utf-8'); print(json.dumps(result,indent=2))
if __name__=='__main__': main()

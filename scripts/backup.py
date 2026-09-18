#!/usr/bin/env python3
import argparse,datetime as dt,json,os
from pathlib import Path
import requests
from dotenv import load_dotenv
load_dotenv()
def main():
 p=argparse.ArgumentParser(); p.add_argument('--url',default=os.getenv('WP_URL')); p.add_argument('--output-dir',default='backup'); a=p.parse_args()
 if not a.url: p.error('Set WP_URL in .env or pass --url')
 base=a.url.rstrip('/'); auth=(os.getenv('WP_USER'),os.getenv('WP_APP_PASSWORD')); stamp=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ'); out=Path(a.output_dir)/stamp; out.mkdir(parents=True,exist_ok=True)
 for filename,ep in {'site.json':'/wp-json/','users-me.json':'/wp-json/wp/v2/users/me?context=edit','pages.json':'/wp-json/wp/v2/pages?per_page=100&context=edit','posts.json':'/wp-json/wp/v2/posts?per_page=100&context=edit','media.json':'/wp-json/wp/v2/media?per_page=100&context=edit'}.items():
  r=requests.get(base+ep,auth=auth,timeout=60); r.raise_for_status(); (out/filename).write_text(json.dumps(r.json(),indent=2),encoding='utf-8')
 (out/'manifest.json').write_text(json.dumps({'site_url':base,'created_utc':stamp,'read_only':True},indent=2),encoding='utf-8'); print(f'Backup created: {out}')
if __name__=='__main__': main()

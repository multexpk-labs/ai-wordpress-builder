#!/usr/bin/env python3
import os,requests
from dotenv import load_dotenv
load_dotenv()
class WordPressClient:
 def __init__(self,base_url=None,user=None,app_password=None): self.base_url=(base_url or os.getenv('WP_URL','')).rstrip('/'); self.auth=(user or os.getenv('WP_USER'),app_password or os.getenv('WP_APP_PASSWORD'))
 def get(self,endpoint,**kwargs): return requests.get(self.base_url+endpoint,auth=self.auth,timeout=kwargs.pop('timeout',30),**kwargs)

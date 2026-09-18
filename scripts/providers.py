import os
from dotenv import load_dotenv
load_dotenv()
def provider_config():
 return {'provider':os.getenv('LLM_PROVIDER','ollama'),'ollama_base_url':os.getenv('OLLAMA_BASE_URL','http://127.0.0.1:11434'),'ollama_model':os.getenv('OLLAMA_MODEL',''),'omnirouter_base_url':os.getenv('OMNIROUTER_BASE_URL',''),'omnirouter_model':os.getenv('OMNIROUTER_MODEL','')}

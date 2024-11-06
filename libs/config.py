import os
import time
from dotenv import load_dotenv

load_dotenv()

tenant_name = os.getenv('TENANT_NAME','rag')

app_version="0.0.1"
app_title = os.getenv('APP_TITLE', 'Demo')
app_password = os.getenv('APP_PASSWORD')

is_debug = os.getenv('DEBUG_MODE') == 'true'
api_key = os.getenv('API_KEY', 'api_key')
update_time = os.getenv('UPDATE_TIME', time.strftime("%Y-%m-%d %H:%M:%S"))

azure_api_key = os.getenv('AZURE_API_KEY', '')
azure_api_base = os.getenv('AZURE_API_BASE', '')
azure_api_version = os.getenv('AZURE_API_VERSION', '')

azure_chat_model_id = os.getenv('AZURE_CHAT_MODEL_ID', 'gpt-4o-mini')
azure_chat_deployment_name = os.getenv('AZURE_CHAT_DEPLOYMENT_NAME', 'gpt-4o-mini')

azure_embedding_model_id = os.getenv('AZURE_EMBEDDING_MODEL_ID', 'text-embedding-3-small')
azure_embedding_deployment_name = os.getenv('AZURE_EMBEDDING_DEPLOYMENT_NAME', 'text-embedding-3-small')

ai_search_url = os.getenv('AI_SEARCH_URL', '')
ai_search_key = os.getenv('AI_SEARCH_KEY', '')

di_url = os.getenv('DI_URL', '')
di_key = os.getenv('DI_KEY', '')

disable_pgvector = os.getenv('DISABLE_PGVECTOR', False)
disable_aisearch = os.getenv('DISABLE_AI_SAERCH', False)

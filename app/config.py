import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "fastapi-chatgpt"

# Choose one method to set your OpenAI API key

# 1. email and password
OPENAPI_EMAIL = os.environ.get("OPENAPI_ACCOUNT", "")
OPENAPI_PASSWORD = os.environ.get("OPENAPI_PASSWORD", "")

# 2. session token
OPENAPI_SESSION_TOKEN = os.environ.get("OPENAPI_SESSION_TOKEN", "")

# 3. access token https://chat.openai.com/api/auth/session
OPENAPI_ACCESS_TOKEN = os.environ.get("OPENAPI_ACCESS_TOKEN", "")

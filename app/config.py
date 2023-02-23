import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "fastapi-chatgpt"

# Choose one method to set your OpenAI API key

# 1. email and password
OPENAI_EMAIL = os.environ.get("OPENAI_ACCOUNT", "")
OPENAI_PASSWORD = os.environ.get("OPENAI_PASSWORD", "")

# 2. session token
OPENAI_SESSION_TOKEN = os.environ.get("OPENAI_SESSION_TOKEN", "")

# 3. access token https://chat.openai.com/api/auth/session
OPENAI_ACCESS_TOKEN = os.environ.get("OPENAI_ACCESS_TOKEN", "")

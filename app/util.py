from fastapi import HTTPException, status
from revChatGPT.V1 import Chatbot

from app.config import OPENAPI_ACCESS_TOKEN, OPENAPI_EMAIL, OPENAPI_PASSWORD, OPENAPI_SESSION_TOKEN
from app.dto import Answer


class GlobalStorage:
    chatbot = None


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def init_chatbot():
    if OPENAPI_EMAIL and OPENAPI_PASSWORD:
        GlobalStorage.chatbot = Chatbot(config={"email": OPENAPI_EMAIL, "password": OPENAPI_PASSWORD})
    elif OPENAPI_SESSION_TOKEN:
        GlobalStorage.chatbot = Chatbot(config={"session_token": OPENAPI_SESSION_TOKEN})
    elif OPENAPI_ACCESS_TOKEN:
        GlobalStorage.chatbot = Chatbot(config={"access_token": OPENAPI_ACCESS_TOKEN})


def chat(prompt: str) -> Answer:
    response = None
    if not GlobalStorage.chatbot:
        init_chatbot()
    if not GlobalStorage.chatbot:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Chatbot not initialized")
    for data in GlobalStorage.chatbot.ask(prompt):
        response = data
    return Answer(**response)


def chat_ws(prompt: str):
    if not GlobalStorage.chatbot:
        init_chatbot()
    if not GlobalStorage.chatbot:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Chatbot not initialized")
    for data in GlobalStorage.chatbot.ask(prompt):
        yield data["message"]

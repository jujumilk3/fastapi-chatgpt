from fastapi import HTTPException, status
from revChatGPT.V1 import Chatbot

from app.config import OPENAI_ACCESS_TOKEN, OPENAI_EMAIL, OPENAI_PASSWORD, OPENAI_SESSION_TOKEN
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
    if OPENAI_EMAIL and OPENAI_PASSWORD:
        GlobalStorage.chatbot = Chatbot(config={"email": OPENAI_EMAIL, "password": OPENAI_PASSWORD})
    elif OPENAI_SESSION_TOKEN:
        GlobalStorage.chatbot = Chatbot(config={"session_token": OPENAI_SESSION_TOKEN})
    elif OPENAI_ACCESS_TOKEN:
        GlobalStorage.chatbot = Chatbot(config={"access_token": OPENAI_ACCESS_TOKEN})


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

from fastapi import Body, FastAPI

from app.config import PROJECT_NAME
from app.dto import Answer
from app.util import Singleton, chat, init_chatbot


class AppCreator(metaclass=Singleton):
    def __init__(self):
        init_chatbot()

        self.app = FastAPI(
            title=PROJECT_NAME,
            openapi_url=f"/openapi.json",
            version="0.0.1",
        )


app_creator = AppCreator()
app = app_creator.app


@app.get("/")
def root():
    return {"status": "OK"}


@app.post("/prompt")
def q(prompt: str = Body("Are you there?", embed=True, description="Prompt")) -> Answer:
    return chat(prompt)

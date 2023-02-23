from pydantic import BaseModel, Field


class Answer(BaseModel):
    message: str = Field(None, description="message", example="Yes, I'm here! How can I assist you today?")
    conversation_id: str = Field(None, description="conversation_id", example="f43d3467-09f7-4019-bf98-141684694d1a")
    parent_id: str = Field(None, description="parent_id", example="a8ee6ae0-4644-4a50-a3f4-c5642595647f")

from pydantic import BaseModel
from typing import Optional


class Message(BaseModel):
    author: str
    msg: str
    

class MessageOut(BaseModel):
    data: list[Message] = []
    error: Optional[Message] = None

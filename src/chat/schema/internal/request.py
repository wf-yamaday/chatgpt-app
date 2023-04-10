from typing import List

from pydantic import BaseModel

from src.chat.entities.chat import Role


class ChatMessage(BaseModel):
    role: Role
    content: str


class ChatStreamRequest(BaseModel):
    query: str
    messages: List[ChatMessage]

    def has_history(self) -> bool:
        return len(self.messages) > 0

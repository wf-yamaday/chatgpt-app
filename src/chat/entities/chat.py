from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field

GPT35Model = Literal["gpt-3.5-turbo", "gpt-3.5-turbo-0301"]
GPT4Model = Literal["gpt-4", "gpt-4-0314", "gpt-4-32k", "gpt-4-32k-0314"]
Role = Literal["system", "user", "assistant"]


class ChatConfig(BaseModel):
    """
    Configuration for the chat model.
    See: https://platform.openai.com/docs/api-reference/chat

    Attributes:
    - temperature: Controls the randomness of the generated responses. Higher values result in more random responses.
    - top_p: Controls the diversity of the generated responses. Lower values result in more diverse responses.
    - n: Controls the number of responses generated.
    - max_tokens: Controls the maximum number of tokens (words) in the generated responses.
    - stop: Controls the sequence of tokens that will stop the response generation.
    - presence_penalty: Controls the tendency of the model to generate unique responses. Lower values result in more unique responses.
    - frequency_penalty: Controls the tendency of the model to generate rare responses. Higher values result in more rare responses.
    - logit_bias: Modify the likelihood of specified tokens appearing in the completion.
    - user: A unique identifier representing your end-user.
    """

    temperature: int = Field(default=1, ge=0, le=2)
    top_p: int = Field(default=1)
    n: int = Field(default=1)
    max_tokens: Optional[int] = Field()
    stop: Optional[Union[str, List[str]]] = Field(default=None)
    presence_penalty: int = Field(default=0, ge=-2, le=2)
    frequency_penalty: int = Field(default=0, ge=-2, le=2)
    logit_bias: Optional[dict] = Field(default=None)
    user: Optional[str] = Field(default=None)


class MessageItem(BaseModel):
    """
    A message in a chat conversation.

    Attributes:
    - role: The role of the sender of the message (system, user, or assistant).
    - content: The text content of the message.
    """

    role: Role
    content: str


class Chat(BaseModel):
    """
    A chat conversation between one or more users and an AI model.

    Attributes:
    - model: The name of the AI model being used in the conversation.
    - messages: A list of MessageItem objects in the conversation.
    - config: The configuration settings for the chat model.
    """

    model: Union[GPT35Model, GPT4Model]
    messages: List[MessageItem]
    config: ChatConfig

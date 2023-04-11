from typing import List, Literal, Optional, TypedDict


class StreamMessageResponse(TypedDict):
    """
    A response message in an OpenAI chat conversation.

    Attributes:
    - role: The role of the sender of the message (system, user, or assistant).
    - content: The text content of the message.
    """

    role: Optional[str]
    content: Optional[str]


class StreamChoiceItemResponse(TypedDict):
    """
    A response choice item in an OpenAI chat conversation.

    Attributes:
    - index: The index of the choice item.
    - delta: The MessageResponse object.
    - finish_reason: The reason for the conversation termination.
    """

    index: int
    delta: StreamMessageResponse
    finish_reason: Optional[str]


class UsageResponse:
    """
    Usage statistics for an OpenAI chat response.

    Attributes:
    - prompt_tokens: The number of tokens in the prompt for the response.
    - completion_tokens: The number of tokens in the generated response.
    - total_tokens: The total number of tokens in the prompt and generated response.
    """

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class OpenAIChatResponse(TypedDict):
    # flake8: noqa
    """
    A response object for an OpenAI chat completion.

    Attributes:
    - id: The identifier for the completion.
    - object: The type of the completion (always "chat.completion").
    - created: The timestamp of the completion creation.
    - choices: A list of ChoiceItemResponse objects representing the response choices for the completion.
    - usage: The UsageResponse object representing the usage statistics for the completion.
    """

    id: str
    object: Literal["chat.completion"]
    created: int
    choices: List[StreamChoiceItemResponse]
    usage: UsageResponse

from typing import Generator, List

import openai

from src.chat.schema.external.openai import OpenAIChatResponse
from src.chat.schema.internal.request import ChatStreamRequest


def generate_stream(payload: ChatStreamRequest) -> Generator[str, None, None]:
    # flake8: noqa
    """
    Generates a chat stream using OpenAI's model based on the user input specified in `payload`.

    Args:
        payload (ChartStreamRequest): An object containing the necessary information to generate a chat stream.

    Yields:
        str: One of the generated chat messages.
    """
    try:
        finish_reason = None
        while not finish_reason:
            if payload.has_history():
                chat_messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    *[message.dict() for message in payload.messages],
                ]
            else:
                chat_messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"{payload.query}"},
                ]

            stream: List[OpenAIChatResponse] = openai.ChatCompletion.create(  # type: ignore
                model="gpt-3.5-turbo",
                messages=chat_messages,
                temperature=1,
                max_tokens=1000,
                stream=True,
            )

            for line in stream:
                finish_reason = line["choices"][0]["finish_reason"]
                if (
                    "content" in line["choices"][0]["delta"]
                    and line["choices"][0]["delta"]["content"] is not None
                ):
                    current_response = line["choices"][0]["delta"]["content"]
                    yield current_response
    except Exception as e:
        error_message = f"Error: {str(e)}"
        yield error_message

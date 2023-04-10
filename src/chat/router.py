from typing import Union

from fastapi import APIRouter
from fastapi.responses import JSONResponse, StreamingResponse

from src.chat.schema.internal.request import ChatStreamRequest

from .service import generate_stream

chat_router = APIRouter()


@chat_router.post("/api/chat/stream/", response_model=None)
async def chat(payload: ChatStreamRequest) -> Union[StreamingResponse, JSONResponse]:
    stream = generate_stream(payload=payload)
    first_item = next(stream)
    if "Error:" in first_item:
        return JSONResponse(status_code=500, content={"detail": first_item})

    return StreamingResponse(
        generate_stream(payload=payload), media_type="text/event-stream"
    )

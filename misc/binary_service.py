import os

from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel, Field

app = FastAPI()


class SomeRequest(BaseModel):
    num: int = Field(default=0)


@app.post("/")
def get_root(request: SomeRequest):
    # validate the request -> done by Pydantic and FastAPI internally
    num_of_bytes = request.num
    output: bytes = os.urandom(num_of_bytes)
    return Response(content=output, media_type="application/octet-stream")

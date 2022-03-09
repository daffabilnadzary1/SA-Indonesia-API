from ninja import Schema
from pydantic import BaseModel

class QueryString(Schema):
    query: str = ''

class QueryList(Schema):
    query: list = None

class ResponseMessage(Schema):
    status: int
    message: str
    payload: dict = {}
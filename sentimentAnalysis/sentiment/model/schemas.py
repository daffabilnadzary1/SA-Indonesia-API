from ninja import Schema

class QueryString(Schema):
    query: str = ''

class QueryList(Schema):
    query: list = None

class ResponseMessage(Schema):
    status: int
    message: str
    payload: dict = {}
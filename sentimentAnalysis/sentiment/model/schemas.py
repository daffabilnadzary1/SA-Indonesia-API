from ninja import Schema


class SentimentOneSchema(Schema):
    text: str
    sentiment: str
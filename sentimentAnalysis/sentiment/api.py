from ninja import NinjaAPI

from django.http import HttpRequest
from django.http import JsonResponse

from .models import Post
from .apps import SentimentConfig
from .schemas import SentimentOneSchema

from rest_framework.views import APIView
from pydantic import BaseModel

api = NinjaAPI()

class QueryString(BaseModel):
    query: str

def predicting(text: str):
    vector = SentimentConfig.vectorizer.transform([text])
    prediction = SentimentConfig.model.predict(vector)

    response = {
        "text_sentiment": prediction[0],
    }
    return response

@api.post('/sentimentone')
def predict_sentiment(request:HttpRequest, query_string: QueryString):

    sentiment = predicting(query_string.query)
    # response = {
    #     "text": query_string.query,
    #     "sentiment":sentiment,
    # }
    return {
        "query": query_string.query,
        "sentiment": sentiment,
    }

# @api.post('sentimentlist')
# def predict_sentiments(request: HttpRequest, query_string: )
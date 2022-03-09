from ninja import NinjaAPI
from django.http import HttpRequest
from django.http import JsonResponse
from sentiment.model.schemas import QueryString, QueryList, ResponseMessage
from sentiment.services.sentiment_service import SentimentPrediction

sentiment_api = NinjaAPI(
    title = 'Indonesian Sentiment Analysis API',
    description = 'API for predicting the sentiment of Indonesian sentence'
)

sentiment_prediction = SentimentPrediction()

@sentiment_api.post('sentimentone', response = {200: ResponseMessage})
def predict_sentiment(request: HttpRequest, query_string: QueryString = QueryString()):

    payload = sentiment_prediction.predicting(query_string.query)
    return 200, {
        'status': 200, 'message': 'OK', 'payload': payload
    }

@sentiment_api.post('sentimentlist', response = {200: ResponseMessage})
def predict_sentiments(request: HttpRequest, query_list: QueryList):
    sentiment = sentiment_prediction.predicting(query_list.query)
    payload = {
        "results": sentiment
    }

    return 200, {
        'status': 200, 'message': 'OK', 'payload': payload
    }
from django.shortcuts import render

from .apps import SentimentConfig
from django.http import JsonResponse
from rest_framework.views import APIView
 
# class call_model(APIView):
#     def get(self, request):
#         if request.method == "GET":
#             text = request.GET.get('text')

#             vector = SentimentConfig.vectorizer.transform([text])
#             prediction = SentimentConfig.model.predict(vector)
#             response = {
#                 "text":text,
#                 "text_sentiment": prediction[0],
#             }

#             return JsonResponse(response)
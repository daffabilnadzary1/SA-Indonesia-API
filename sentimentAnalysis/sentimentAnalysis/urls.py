from django.contrib import admin
from django.urls import path
from sentiment.controller.predicting_controller import sentiment_api

urlpatterns = [
    path('predict/', sentiment_api.urls)
]

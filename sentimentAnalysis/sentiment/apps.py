from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class SentimentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sentiment'

    path = os.path.join(settings.MODELS, 'sentiment_models.p')
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    model = data["model"]
    vectorizer = data["vectorizer"]

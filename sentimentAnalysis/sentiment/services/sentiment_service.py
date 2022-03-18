from .sentiment_config import SentimentConfig
from .preprocessing_service import preprocessing

class SentimentPrediction():
    def __init__(self) -> None:
        pass

    def predicting(self, text):
        if isinstance(text, str):
            text = preprocessing(text)
            vector = SentimentConfig.vectorizer.transform([text])
            prediction = SentimentConfig.model.predict(vector)

            response = {
                "query": text,
                "text_sentiment": prediction[0],
            }
            return response
        elif isinstance(text, list):
            results = []
            for x in text:
                x = preprocessing(x)
                vector = SentimentConfig.vectorizer.transform([x])
                prediction = SentimentConfig.model.predict(vector)

                results.append(
                    {
                        "text": x,
                        "text_sentiment": prediction[0],
                    }
                )
            return results
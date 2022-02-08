from django.db import models

class Post(models.Model):
    text = models.CharField(max_length = 100)
    sentiment = models.CharField(max_length = 100)

    def __str__(self):
        return self.sentiment
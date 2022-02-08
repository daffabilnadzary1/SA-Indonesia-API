from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from sentiment import views
from sentiment.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("classifyOne/", views.call_model.as_view())
    path('predict/', api.urls)
]

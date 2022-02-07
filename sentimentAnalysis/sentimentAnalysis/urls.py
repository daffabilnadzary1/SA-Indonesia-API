from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from sentiment import views

api = NinjaAPI()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("classify/", views.call_model.as_view()),
]

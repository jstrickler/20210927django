from django.urls import path
from . import views

app_name = "goodbye"

urlpatterns = [
    path('', views.goodbye, name="goodbye"),
]

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fancy_phone_number, name='fancy_phone_number'),
]

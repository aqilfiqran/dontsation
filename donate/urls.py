from django.contrib import admin
from django.urls import path, include
from .views import Index

app_name = "donate"
urlpatterns = [
    path('', Index, name="index")
]

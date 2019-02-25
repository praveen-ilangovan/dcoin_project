from django.contrib import admin
from django.urls import path

from . import views

app_name = "dcoin_app"

urlpatterns = [
    path('', views.register, name='register'),
]

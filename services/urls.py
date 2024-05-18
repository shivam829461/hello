from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ServicePageView

urlpatterns = [
    path('', ServicePageView.as_view(), name='services'),
]
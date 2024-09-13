"""
This file is used to define the URL patterns for the main app.
"""
from django.urls import path
from .views import index, find_entities

urlpatterns = [
    path('', index, name='home'),
    path('search_entity', find_entities, name='search-entities'),
]


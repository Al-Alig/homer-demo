"""
This file is used to define the URL patterns for the entity app.
"""

from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.create_application),
    path('entity/<int:entity_id>/', views.entity_detail, name='entity_detail'),
    path('reservations', views.reservations),
]

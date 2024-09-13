"""
This file is used to configure the app name for the reviews app.
"""
from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """
    This class is used to configure the app name for the reviews app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'

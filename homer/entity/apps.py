"""
This file is used to configure the entity app.
"""

from django.apps import AppConfig


class EntityConfig(AppConfig):
    """
    Entity app config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entity'

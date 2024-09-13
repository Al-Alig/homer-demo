"""
This file is used to register the models in the admin panel.
"""

from django.contrib import admin
from entity.models import Order, Entity

# Register your models here.
admin.site.register(Order)
admin.site.register(Entity)

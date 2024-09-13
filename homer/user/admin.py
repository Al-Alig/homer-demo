"""
This file is used to register the User model in the admin panel.
"""
from django.contrib import admin

from user.models import User

# Register your models here.
admin.site.register(User)

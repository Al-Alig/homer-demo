"""
This file contains the User model.
"""
from django.contrib.auth.models import AbstractUser as djangoUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(djangoUser):
    """
    This class is used to create the User model.
    """

    id = models.BigAutoField(primary_key=True)

    profile_photo = models.ImageField(
        upload_to="profile_photos/",
        default="profile_photos/default.png"
    )

    country = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)

    first_name = models.CharField(_("first name"), max_length=30, null=True)
    last_name = models.CharField(_("last name"), max_length=30, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=15, null=True)

    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"

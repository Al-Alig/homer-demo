"""
This module contains the Review model.
"""
from django.db import models

from entity.models import Entity
from user.models import User


# Create your models here.

class Review(models.Model):
    """
    This class is used to create a Review model.
    """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=50)
    body = models.TextField()
    rating = models.IntegerField()

    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.title} to {self.entity.name}"

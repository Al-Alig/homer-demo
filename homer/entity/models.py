"""
Models for db related with entity app
"""

from django.db import models
from django_enum import EnumField

from user.models import User


# Create your models here.
class Entity(models.Model):
    """
    Entity model
    """
    class TypeEnum(models.IntegerChoices):
        """
        Enum for entity types
        """

        HOUSE = 1, 'HOUSE'
        APARTMENT = 2, 'APARTMENT'
        ROOM = 3, 'ROOM'
        OFFICE = 4, 'OFFICE'
        LAND = 5, 'LAND'
        OTHER = 6, 'OTHER'

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)

    entity_image = models.ImageField(upload_to="entity", default="entity/image.svg")

    type = EnumField(TypeEnum)
    description = models.TextField()
    price = models.FloatField()

    city = models.CharField(max_length=30)
    country = models.CharField(max_length=2)
    address = models.CharField(max_length=200)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.user.get_full_name()} - {self.country}"


class Order(models.Model):
    """
    Order model
    """
    class StatusEnum(models.IntegerChoices):
        """
        Enum for order status
        """
        PENDING = 1, 'PENDING'
        ACCEPTED = 2, 'ACCEPTED'
        REJECTED = 3, 'REJECTED'
        CLOSED = 4, 'CLOSED'

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    creation_date = models.DateField(auto_now=True)
    start_date = models.DateField()
    close_date = models.DateField()

    status = EnumField(StatusEnum)

    def __str__(self):
        return (f'{self.id} - {self.entity.name} - {self.creation_date}'
                f' - {self.user.get_full_name()}')


class EntityImages(models.Model):
    """
    Entity images model
    """

    id = models.BigAutoField(primary_key=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='entity')

from django.db import models

__all__ = (
    'Place',
    'Restaurant',
)


class Place(models.Model):
    name = models.CharField(max_length=50, default='ABC')
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} Restaurant'
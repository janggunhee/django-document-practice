from django.db import models

__all__ = (
    'Pizza',
    'Topping',
    'TwitterUser',
)


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name

class TwitterUser(models.Model):
    # 자기자신 (TwitterUser ('self'))를 참조해서
    # friends 필더를 MTM으로 정의
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField(
        'self',
        blank=True,
    )

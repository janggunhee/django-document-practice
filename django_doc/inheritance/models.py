from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    class Mata:
        abstract =True



class Teacher(CommonInfo):
    subject = models.CharField(max_length=30)



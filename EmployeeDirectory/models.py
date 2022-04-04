from django.db import models


class Employee(models.Model):

    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    office_location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


from django.db import models


class Visitor(models.Model):

    objects = None
    visitor_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobile_no = models.CharField(max_length=15)
    office_location = models.CharField(max_length=100)
    visitor_host = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    arrival_date = models.DateField()
    departure_time = models.TimeField(null=True, blank=True)
    departure_date = models.DateField(null=True, blank=True)
    visitor_status = models.CharField(max_length=100)



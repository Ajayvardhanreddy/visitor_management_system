from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Employee
        fields = ['name', 'email', 'office_location', 'department']
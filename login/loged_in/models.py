from enum import auto
from django.db import models

class userData(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    DOB=models.DateField()
    mobile=models.BigIntegerField()
    email_id=models.EmailField(max_length=200)
    user=models.CharField(max_length=10)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
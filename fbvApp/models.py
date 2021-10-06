from django.db import models


# Create your models here.
class Student(models.Model):
    objects = None
    firstName = models.CharField(max_length=20)
    Topic=models.CharField(max_length=20,default="None")
    lastName = models.TextField(max_length=2000)
    testScore = models.FloatField()


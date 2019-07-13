from django.db import models
class addressdata(models.Model):
    name=models.CharField(max_length=100)
    mobileno=models.BigIntegerField()
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=100)


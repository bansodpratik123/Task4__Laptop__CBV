from django.db import models

# Create your models here.
class Laptops(models.Model):
    Model_Name=models.CharField(max_length=32)
    Company=models.CharField(max_length=32)
    RAM=models.IntegerField()
    ROM=models.IntegerField()
    Processor=models.CharField(max_length=32)
    Weight=models.FloatField()
    Price=models.FloatField()
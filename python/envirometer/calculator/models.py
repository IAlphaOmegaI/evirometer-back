from django.db import models

# Create your models here.
class Book(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=100)
        type = models.CharField(max_length=100)
        description = models.DateField()
        carbon_emited = models.CharField(max_length=13)
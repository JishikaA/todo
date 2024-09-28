from django.db import models

# Create your models here.
class Todo1(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    date_field = models.DateField()
from django.db import models

# Create your models here.


class accounts(models.Model):
    username = models.CharField(max_length=100)
    password = models.models.CharField(min_length=8)
    
from django.db import models

# Create your models here.

class summoner_name(models.Model):
    summoner_name = models.CharField(max_length=30)
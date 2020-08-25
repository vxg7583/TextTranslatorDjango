from django.db import models

# Create your models here.

class Translator(models.Model):
    text = models.TextField(max_length=1000)
    ids = models.IntegerField(default=0)

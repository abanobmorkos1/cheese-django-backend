from django.db import models

class cheeseAttr(models.Model):
    name = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
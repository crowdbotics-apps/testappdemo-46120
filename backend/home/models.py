from django.conf import settings
from django.db import models


class News(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=255,
    )
    age = models.IntegerField()

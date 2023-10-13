from django.db import models


class Keyword(models.Model):
    name = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class Trend(models.Model):
    name = models.TextField()
    result = models.IntegerField()
    search_period = models.TextField()
    created_at = models.DateField(auto_now_add=True)

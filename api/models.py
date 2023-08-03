from django.db import models
from django.utils import timezone


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(choices=((0,'Low'), (1,'Medium'),(2,'High')))
    crated_at = models.DateTimeField(default=timezone.now)
    expired_at = models.DateTimeField(null=True, blank=True)


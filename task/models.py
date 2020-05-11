from django.db import models
from django.utils import timezone


class Task(models.Model):
    ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    dl = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
    done = models.BooleanField(default=False)

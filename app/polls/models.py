import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


# Create your models here.
class Poll(models.Model):
    poll_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

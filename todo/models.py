"""
Definition of models.
"""

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    endorsement = models.PositiveSmallIntegerField(help_text="Please specify the amount of Achiever Points that will be rewarded on completion", default=0)
    task_description = models.CharField(max_length=250, help_text="Please provide a short description of the task.", default="")
    motivation = models.CharField(max_length=250, help_text="Please provide the motivation behind the task.", default="")
    time_estimate = models.DurationField(help_text="Please specify how long the task is estimated to take.", default=0)
    additional_information = models.TextField(max_length=1000, help_text="Please provide additional information that can help understanding the task's breadth and stakes", blank=True)
    attachments = models.FileField(upload_to='uploads/', blank=True)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title

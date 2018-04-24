"""
Definition of models.
"""

from datetime import datetime
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200, unique=True)
    owner = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, verbose_name="Owner")
    endorsement = models.PositiveSmallIntegerField(verbose_name="Endorsement", help_text="Please specify the amount of Achiever Points that will be rewarded on completion", default=0, blank=False)
    task_description = models.CharField(verbose_name="Task description", max_length=250, help_text="Please provide a short description of the task.", default="", blank=False)
    motivation = models.CharField(verbose_name="Motivation", max_length=250, help_text="Please provide the motivation behind the task.", default="", blank=False)
    time_estimate = models.DurationField(verbose_name="Time estimate", help_text="Please specify how long the task is estimated to take.", default=timedelta(0), blank=False)
    additional_information = models.TextField(verbose_name="Additional information", max_length=1000, help_text="Please provide additional information that can help understanding the task's breadth and stakes", blank=True)
    attachments = models.FileField(verbose_name="Attachments", upload_to='uploads/', blank=True)
    created_at = models.DateTimeField(verbose_name="Created at", default=0, blank=False)

    def __str__(self):
        return self.title

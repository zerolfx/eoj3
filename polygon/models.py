from django.db import models
from account.models import User
from problem.models import Problem


class EditSession(models.Model):

    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    fingerprint = models.CharField(max_length=64)
    problem = models.ForeignKey(Problem)
    last_synchronize = models.DateTimeField(blank=True)

    class Meta:
        ordering = ["-last_synchronize"]
        unique_together = ["user", "problem"]  # You can have only one session.


class Run(models.Model):

    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

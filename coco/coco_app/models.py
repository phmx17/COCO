from django.db import models
from django.contrib.auth.models import User  # using default User for now
import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d") # separates date from time and formats. can use . or / or whatever

class Time(models.Model):
    date = models.DateField(default=current_date)
    time = models.FloatField(default=0.0)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, blank=True, null=True)
    # to string method
    def __str__(self):
        return f"{self.date} {self.time} {self.project.title} {self.developer} {self.comments}"


class Project(models.Model):
    short_cut = models.CharField(max_length=100, default='none')
    title = models.CharField(max_length=100, default='none')

    def __str__(self):
        return f"{self.title}"




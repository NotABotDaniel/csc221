from django.db import models

# Create your models here.

class Task(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return "[X] " + self.name if self.completed else "[  ] " + self.name
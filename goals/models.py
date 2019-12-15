from django.db import models
from django.utils import timezone

# Create your models here.
class DailyGoals(models.Model):
    entryDate = models.DateField(default=timezone.now())
    title = models.CharField(max_length=150)
    isComplete = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.title

class DailyNote(models.Model):
    entryDate = models.DateField(default=timezone.now(), unique=True)
    content = models.TextField()

    def __str__(self):
        return self.content

class MainGoals(models.Model):
    creationDate = models.DateField(default=timezone.now())
    isLongTerm = models.BooleanField(default=False)
    title = models.CharField(max_length=150)
    isComplete = models.BooleanField(default=False, null=False)
    completeDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

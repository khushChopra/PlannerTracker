from django.db import models
from django.utils.timezone import now

# Create your models here.
class Habit(models.Model):
    title = models.CharField(max_length=150)
    habitIsDecimal = models.BooleanField(null=False)
    creationDate = models.DateField(default=now)
    endDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class HabitEntryBool(models.Model):
    habit = models.ForeignKey(
        Habit,
        on_delete = models.CASCADE
    )
    entryDate = models.DateField(blank=False, null=False, default=now)

    def __str__(self):
        return self.habit.__str__() + ' ' + str(self.entryDate)
    
class HabitEntryDecimal(models.Model):
    habit = models.ForeignKey(
        Habit,
        on_delete = models.CASCADE
    )
    value = models.DecimalField(max_digits=4, decimal_places=1) 
    entryDate = models.DateField(blank=False, null=False, default=now)

    def __str__(self):
        return self.habit.__str__() + ' ' + str(self.entryDate)
    
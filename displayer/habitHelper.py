from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.dateformat import format
from django.utils.dates import WEEKDAYS_ABBR
from habits.models import Habit, HabitEntryBool, HabitEntryDecimal

# Create your views here.
def getHabitData():
    # Get all active habits
    allActiveHabits = Habit.objects.filter(endDate=None)

    # last7Dates
    last7Dates = [datetime.now()-timedelta(days=x) for x in range(7)][::-1]
    last7Days = [WEEKDAYS_ABBR[x.weekday()] for x in last7Dates]
    
    # habit entries for last 7 days for each entry 
    entryData = []
    for habit in allActiveHabits:
        tempArray = []
        for thisDate in last7Dates:
            if habit.habitIsDecimal:
                try:
                    habitEntry = HabitEntryDecimal.objects.get(habit=habit, entryDate=thisDate)
                except HabitEntryDecimal.DoesNotExist:
                    habitEntry = None
            else:
                try:
                    habitEntry = HabitEntryBool.objects.get(habit=habit, entryDate=thisDate)
                except HabitEntryBool.DoesNotExist:
                    habitEntry = None
            tempArray.append(habitEntry)
        todaySet = False
        if tempArray[-1]:
            todaySet = True
        entryData.append( (habit,  tempArray, todaySet) )

    return entryData, last7Days, last7Dates
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.dateformat import format
from django.utils.dates import WEEKDAYS_ABBR
from habits.models import Habit, HabitEntryBool, HabitEntryDecimal
from goals.models import DailyNote, DailyGoals, MainGoals
from .habitHelper import getHabitData
from .goalHelper import getDailyNote, getMainGoals


# Create your views here.
def homeView(request):
    # Get all active habit's data
    entryData, last7Days, last7Dates = getHabitData()

    # todays note
    todaysNote = getDailyNote()

    # main goals
    listMainGoalst1, listMainGoalst2 = getMainGoals()

    # get last 2 and next 4 days
    # format for table display
    dailyGoalData = []
    weekStart = 0
    while (datetime.now()+timedelta(days=weekStart)).isoweekday()!=1:
        weekStart -=1
    for day in [datetime.now()+timedelta(days=x) for x in range(weekStart,weekStart+7)]:
        goals = DailyGoals.objects.filter(entryDate=day)
        dailyGoalData.append((format(day, "D, d M"), goals)) 
    
    # todays day, and date

    today = datetime.now()
    today = format(today, "D, d M Y")
    todaysDay = datetime.now().isoweekday()
    context = {
        'today': today,
        'todaysDay': todaysDay,
        'entryData': entryData,
        'last7Dates': last7Dates,
        'last7Days': last7Days,
        'todaysNote': todaysNote,
        'listMainGoalst1': listMainGoalst1,
        'listMainGoalst2': listMainGoalst2,
        'dailyGoalData': dailyGoalData,
    }
    return render(request, 'home.html', context)

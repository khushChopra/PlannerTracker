from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.dateformat import format
from django.utils.dates import WEEKDAYS_ABBR
from habits.models import Habit, HabitEntryBool, HabitEntryDecimal
from goals.models import DailyNote, DailyGoals, MainGoals
from .habitHelper import getHabitData
from .goalHelper import getDailyNote


# Create your views here.
def homeView(request):
    # Get all active habit's data
    entryData, last7Days, last7Dates = getHabitData()

    # todays note
    todaysNote = getDailyNote()

    # main goals
    ## get teir 1 goals
    listMainGoalst1 = MainGoals.objects.filter(isComplete = False, isLongTerm=True)
    ## get tier 2 goals
    listMainGoalst2 = MainGoals.objects.filter(isComplete = False, isLongTerm=False)

    

    context = {
        'timenow': timezone.now(),
        'entryData': entryData,
        'last7Dates': last7Dates,
        'last7Days': last7Days,
        'todaysNote': todaysNote,
        'listMainGoalst1': listMainGoalst1,
        'listMainGoalst2': listMainGoalst2,
    }
    return render(request, 'home.html', context)

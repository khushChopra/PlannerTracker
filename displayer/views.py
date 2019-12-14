from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.dateformat import format
from django.utils.dates import WEEKDAYS_ABBR
from habits.models import Habit, HabitEntryBool, HabitEntryDecimal
from .habitHelper import getHabitData


# Create your views here.
def homeView(request):
    # Get all active habit's data
    entryData, last7Days, last7Dates = getHabitData()

    context = {
        'timenow': timezone.now(),
        'entryData': entryData,
        'last7Dates': last7Dates,
        'last7Days': last7Days
    }
    return render(request, 'home.html', context)

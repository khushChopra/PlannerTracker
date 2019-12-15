from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.dateformat import format
from django.utils.dates import WEEKDAYS_ABBR
from goals.models import DailyNote, DailyGoals, MainGoals

# Create your views here.
def getDailyNote():
    try:
        todaysNote = DailyNote.objects.get(entryDate=datetime.now())
    except Exception as e:
        todaysNote = DailyNote(content="")
    return todaysNote
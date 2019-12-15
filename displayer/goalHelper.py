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

def getMainGoals():
    ## get teir 1 goals
    listMainGoalst1 = MainGoals.objects.filter(isComplete = False, isLongTerm=True)
    listMainGoalst1 |= MainGoals.objects.filter(isComplete = True, isLongTerm=True, completeDate=datetime.now())
    
    ## get tier 2 goals
    listMainGoalst2 = MainGoals.objects.filter(isComplete = False, isLongTerm=False)
    listMainGoalst2 |= MainGoals.objects.filter(isComplete = True, isLongTerm=False, completeDate=datetime.now())
    return listMainGoalst1, listMainGoalst2
from django.shortcuts import render, get_object_or_404
from .models import DailyGoals, DailyNote, MainGoals
from django.utils import timezone
from datetime import datetime, timedelta
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.dateformat import format
from django.views.generic import CreateView

# Create your views here.
def createOrUpdateDailyNote(request, today):
    myDailyNote = None
    try:
        myDailyNote = DailyNote.objects.get(entryDate=today)
    except Exception as e:
        pass
    
    # create or update
    if myDailyNote == None:
        myDailyNote = DailyNote(content=request.POST.get('content'))
    else:
        myDailyNote.content = request.POST.get('content')
    myDailyNote.save()
    print(myDailyNote.content, str(myDailyNote.entryDate))

    return HttpResponseRedirect(reverse('home'))

class CreateMainGoal(CreateView):
    model = MainGoals
    template_name = "maingoalform.html"
    fields = ['isLongTerm','title']
    success_url = reverse_lazy('home')

def markMainGoalDone(request, pk):
    myMainGoal = MainGoals.objects.get(pk=pk)
    myMainGoal.isComplete = True
    myMainGoal.completeDate = datetime.now()
    myMainGoal.save()
    return HttpResponseRedirect(reverse('home'))

class createDailyGoal(CreateView):
    model = DailyGoals
    template_name = "maingoalform.html"
    fields = '__all__'
    success_url = reverse_lazy('home')

def markDailyGoalDone(request, pk):
    myDailyGoal = DailyGoals.objects.get(pk=pk)
    myDailyGoal.isComplete = True
    myDailyGoal.save()
    return HttpResponseRedirect(reverse('home'))

def addDailyGoal(request, day):
    entryDate = getDateFromString(day)
    entryDate = format(entryDate, 'Y-m-d')
    print(entryDate)

    context = {
        'entryDate': entryDate
    }

    return render(request, 'dailygoalform.html', context=context)

def getDateFromString(date, today=datetime.now()):
    weekStart = 0
    while (today+timedelta(days=weekStart)).isoweekday()!=1:
        weekStart -=1
    
    for day in [today+timedelta(days=x) for x in range(weekStart,weekStart+7)]:
        if date == format(day, "D, d M"):
            return day

def getDateFromString2(date):
    weekStart = 0
    while (datetime.now()+timedelta(days=weekStart)).isoweekday()!=1:
        weekStart -=1
    
    for day in [datetime.now()+timedelta(days=x) for x in range(weekStart,weekStart+7)]:
        if date == format(day, "Y-m-d"):
            return day

def submitDailyGoal(request):
    entryDate = getDateFromString2(request.POST.get('entryDate'))
    title = request.POST.get('title')
    datetime.date
    # if title is special
    if '|' in title or ';' in title:
        dailyGoals = title.split(';')
        for dailys in dailyGoals:
            for goal in dailys.split('|'):
                DailyGoals.objects.create(entryDate=entryDate, title=goal, isComplete=False)
            entryDate = entryDate + timedelta(days=1)

    else:
    # if title is not special
        DailyGoals.objects.create(entryDate=entryDate, title=title, isComplete=False)
    return HttpResponseRedirect(reverse('home'))
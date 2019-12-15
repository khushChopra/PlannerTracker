from django.shortcuts import render, get_object_or_404
from .models import DailyGoals, DailyNote, MainGoals
from django.utils import timezone
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
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
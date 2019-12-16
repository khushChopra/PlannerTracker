from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Habit, HabitEntryBool, HabitEntryDecimal
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
class CreateHabit(CreateView):
    model = Habit
    template_name = 'form.html'
    fields = ['title','habitIsDecimal']
    success_url = reverse_lazy('home')

def deleteHabit(request, pk):
    myHabit = Habit.objects.get(pk=pk)
    myHabit.endDate = timezone.now()
    myHabit.save()
    return HttpResponseRedirect(reverse('home'))

def createHabitEntryBool(request, pk):
    myHabit = Habit.objects.get(pk=pk)
    HabitEntryBool.objects.create(habit=myHabit)
    return HttpResponseRedirect(reverse('home'))

def createHabitEntryDeciaml(request, pk):
    myHabit = Habit.objects.get(pk=pk)
    HabitEntryDecimal.objects.create(habit=myHabit, value=request.POST.get('entryVal'))
    return HttpResponseRedirect(reverse('home'))

from django.contrib import admin
from .models import Habit, HabitEntryBool, HabitEntryDecimal


# Register your models here.
admin.site.register(Habit)
admin.site.register(HabitEntryBool)
admin.site.register(HabitEntryDecimal)

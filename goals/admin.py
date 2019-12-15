from django.contrib import admin
from .models import DailyGoals, DailyNote, MainGoals

# Register your models here.
admin.site.register(DailyNote)
admin.site.register(DailyGoals)
admin.site.register(MainGoals)
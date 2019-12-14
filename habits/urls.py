from django.urls import path, include
from .views import CreateHabit, deleteHabit, createHabitEntryBool, createHabitEntryDeciaml

app_name = 'habit'
urlpatterns = [
    path('habit/create', CreateHabit.as_view(), name="create"),
    path('habit/<int:pk>/delete', deleteHabit, name="deleteHabit"),
    path('habit/<int:pk>/createBoolEntry', createHabitEntryBool, name="createHabitEntryBool"),
    path('habit/<int:pk>/createDeciamlEntry', createHabitEntryDeciaml, name="createHabitEntryDeciaml"),
]

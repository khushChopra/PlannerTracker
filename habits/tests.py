from django.test import TestCase
from datetime import datetime, timedelta
from django.urls import reverse
from .models import Habit, HabitEntryBool, HabitEntryDecimal

# Create your tests here.
class ModelTest(TestCase):
    def test_habit(self):
        Habit.objects.create(title="my title", habitIsDecimal=False)
        fromRead = Habit.objects.all()[0]
        self.assertEqual(fromRead.title, "my title")
        self.assertEqual(fromRead.habitIsDecimal, False)
        self.assertIsNone(fromRead.endDate)
        self.assertEqual(fromRead.creationDate, datetime.now().date(), "Default creation date not correct")

    def test_habit_entry_bool(self):
        Habit.objects.create(title="my title", habitIsDecimal=False)
        habitFromRead = Habit.objects.all()[0]
        HabitEntryBool.objects.create(habit=habitFromRead)
        entryFromRead = HabitEntryBool.objects.all()[0]
        self.assertEqual(entryFromRead.entryDate, datetime.now().date())
        self.assertEqual(entryFromRead.habit, habitFromRead)
        habitFromRead.delete()
        self.assertEqual(len(HabitEntryBool.objects.all()), 0)

    def test_habit_entry_decimal(self):
        Habit.objects.create(title="my title", habitIsDecimal=False)
        habitFromRead = Habit.objects.all()[0]
        HabitEntryDecimal.objects.create(habit=habitFromRead, value=12.47)
        entryFromRead = HabitEntryDecimal.objects.all()[0]
        self.assertEqual(entryFromRead.entryDate, datetime.now().date())
        self.assertEqual(entryFromRead.habit, habitFromRead)
        self.assertEqual(str(entryFromRead.value), '12.5')
        habitFromRead.delete()
        self.assertEqual(len(HabitEntryDecimal.objects.all()), 0)

class ViewsTest(TestCase):
    
    def test_create_habit(self):
        response = self.client.get(reverse('habit:create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Title")
        self.assertContains(response, "HabitIsDecimal")
        self.assertTemplateUsed(response, "form.html")

    def test_delete_habit(self):
        # deleteing while empty
        response = self.client.get(reverse('habit:deleteHabit', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 404)

        # inserting into db
        Habit.objects.create(title="my title", habitIsDecimal=False)
        prev = Habit.objects.get(pk=1)
        response = self.client.get(reverse('habit:deleteHabit', kwargs={'pk':1}))
        modified = Habit.objects.get(pk=1)
        self.assertEqual(response.status_code, 302)
        self.assertIsNone(prev.endDate)
        self.assertEqual(modified.endDate, datetime.now().date())
        self.assertRedirects(response, reverse('home'))

    def test_create_entry_bool(self):
        # without any habit entry
        response = self.client.get(reverse("habit:createHabitEntryBool", kwargs={'pk':1}))
        self.assertEqual(response.status_code,404)

        # for non decimal habit
        myHabit = Habit.objects.create(title="my title", habitIsDecimal=False)
        self.assertEqual(len(HabitEntryBool.objects.filter(habit=myHabit)), 0)
        response = self.client.get(reverse("habit:createHabitEntryBool", kwargs={'pk':1}))
        self.assertEqual(response.status_code,302)
        self.assertEqual(len(HabitEntryBool.objects.filter(habit=myHabit, entryDate=datetime.now())),1)
        self.assertRedirects(response, reverse('home'))

        # re request

        response = self.client.get(reverse("habit:createHabitEntryBool", kwargs={'pk':1}))
        self.assertEqual(response.status_code,302)
        self.assertEqual(len(HabitEntryBool.objects.filter(habit=myHabit, entryDate=datetime.now())),1)
        self.assertRedirects(response, reverse('home'))

    def test_create_entry_bool2(self):
        # decimal habit
        myHabit = Habit.objects.create(title="my title", habitIsDecimal=True)
        self.assertEqual(len(HabitEntryBool.objects.filter(habit=myHabit)), 0)
        response = self.client.get(reverse("habit:createHabitEntryBool", kwargs={'pk':1}))
        self.assertEqual(response.status_code,302)
        self.assertEqual(len(HabitEntryBool.objects.filter(habit=myHabit, entryDate=datetime.now())),0)
        self.assertRedirects(response, reverse('home'))

        # re request
        response = self.client.get(reverse("habit:createHabitEntryBool", kwargs={'pk':1}))
        self.assertEqual(response.status_code,302)
        self.assertEqual(len(HabitEntryBool.objects.filter(habit=myHabit, entryDate=datetime.now())),0)
        self.assertRedirects(response, reverse('home'))

    def test_create_entry_decimal(self):
        # without any habit entry
        response = self.client.get(reverse("habit:createHabitEntryDeciaml", kwargs={'pk':1}))
        self.assertEqual(response.status_code,404)

        # for non decimal habit
        myHabit = Habit.objects.create(title="my title", habitIsDecimal=False)
        self.assertEqual(len(HabitEntryDecimal.objects.filter(habit=myHabit)), 0)
        response = self.client.get(reverse("habit:createHabitEntryDeciaml", kwargs={'pk':1}))
        self.assertEqual(response.status_code,302)
        self.assertEqual(len(HabitEntryDecimal.objects.filter(habit=myHabit, entryDate=datetime.now())),0)
        self.assertRedirects(response, reverse('home'))

        # re request
        response = self.client.get(reverse("habit:createHabitEntryDeciaml", kwargs={'pk':1}))
        self.assertEqual(response.status_code,302)
        self.assertEqual(len(HabitEntryDecimal.objects.filter(habit=myHabit, entryDate=datetime.now())),0)
        self.assertRedirects(response, reverse('home'))

    def test_create_entry_decimal2(self):
        # for decimal habit
        myHabit = Habit.objects.create(title="my title", habitIsDecimal=True)
        self.assertEqual(len(HabitEntryDecimal.objects.filter(habit=myHabit)), 0)

        response = self.client.post(reverse("habit:createHabitEntryDeciaml", kwargs={'pk':1}), {'entryVal': 13.7})
        self.assertEqual(response.status_code,302)
        self.assertEqual(len(HabitEntryDecimal.objects.filter(habit=myHabit, entryDate=datetime.now())),1)
        self.assertEqual(str(HabitEntryDecimal.objects.filter(habit=myHabit, entryDate=datetime.now())[0].value),'13.7')
        self.assertRedirects(response, reverse('home'))

        # re request
        response = self.client.post(reverse("habit:createHabitEntryDeciaml", kwargs={'pk':1}), {'entryVal': 13.7})
        self.assertEqual(response.status_code,302)
        self.assertEqual(len(HabitEntryDecimal.objects.filter(habit=myHabit, entryDate=datetime.now())),1)
        self.assertRedirects(response, reverse('home'))
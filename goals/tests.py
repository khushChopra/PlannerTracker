from django.test import TestCase
from .views import getDateFromString
from django.utils.dateformat import format
from datetime import datetime, timedelta

# Create your tests here.
class OneTest(TestCase):
    def test_getDateFromString(self):
        today = datetime.now()
        weekStart = 0
        while (today+timedelta(days=weekStart)).isoweekday()!=1:
            weekStart -=1
        today = today + timedelta(days=weekStart)
        for i in range(0,2*366,7):
            weekStartDay = today + timedelta(days=i)
            for j in range(0,7):
                a = weekStartDay + timedelta(days=j)
                for k in range(0,7):
                    b = weekStartDay + timedelta(days=k)
                    self.assertEqual( getDateFromString( format(b, "D, d M") , a).date(), b.date() )
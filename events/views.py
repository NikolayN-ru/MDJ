from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import *
from .tasks import text


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {'event_list': event_list})


def index(request, year=date.today().year, month=date.today().month):
    text.delay()
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = 'My club event calendar - %s %s' % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    announcements = [
        {
            'date':'6-10-2020',
            'announcement': "Club Registrations Open"
        },
        {
            'date': '6-15-2020',
            'announcement': 'Joe Smith Elected New Club President'
        }
    ]
    return render(request, 'events/calendar_base.html', {'title':title, 'cal':cal, 'announcements':announcements})

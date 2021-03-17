from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('events/', all_events, name='all_events'),
    # path('<int:year>/<str:month>/', index, name='index'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', index, name='index'),
]

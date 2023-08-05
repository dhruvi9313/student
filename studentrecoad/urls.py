from django.urls import path
from .views import *

urlpatterns = [

    path('home/', home),
    path('datetime/', date1),
    path('index/', index),
    path('create/',create),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('airlines/', AirLinesDisplay.as_view(), name= 'AirLines List')
]
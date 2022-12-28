from django.urls import path
from .views import *

urlpatterns = [
    path('airlines/', AirLineDisplaY.as_view(), name= 'AirLines List')
]
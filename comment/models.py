from django.db import models
from residence.models import *
from air.models import *
from abstract.models import AbstractComment


class AirLineComment(AbstractComment):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='airline_comment')


class AirPortComment(AbstractComment):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='airport_comment')


class ResidentialComment(AbstractComment):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name='residential_comment')


class HotelComment(AbstractComment):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_comment')


class HotelRoomComment(AbstractComment):
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='hotel_room_comment')


from django.db import models
from air.models import *


class Flight(models.Model):
    SCHEDULED = 0
    CHARTER = 1
    FLIGHT_TYPE_CHOICE = (
        (SCHEDULED, 'scheduled'),
        (CHARTER, 'charter')
    )

    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    flight_number = models.PositiveIntegerField(verbose_name='Flight Number')
    flight_type = models.BooleanField(choices=FLIGHT_TYPE_CHOICE, default=SCHEDULED, verbose_name='Flight Type')

    start_time = models.DateTimeField(verbose_name='Start Time')
    duration = models.TimeField(null=True, blank=True)

    capacity = models.PositiveSmallIntegerField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.DO_NOTHING)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='flight_airplane')


class FlightTicket(models.Model):
    ECONOMY = 1
    BUSINESS = 2
    FIRST = 3
    FLIGHT_CLASS_CHOICE = (
        (ECONOMY, 'economy'),
        (BUSINESS, 'business'),
        (FIRST, 'first')
    )
    id = models.AutoField(primary_key=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_number_for_ticket')
    flight_class = models.PositiveSmallIntegerField(choices=FLIGHT_CLASS_CHOICE, default=1, verbose_name='Flight Class')
    price_for_one_passenger = models.PositiveIntegerField(default=1, verbose_name='Price for 1 Passenger')



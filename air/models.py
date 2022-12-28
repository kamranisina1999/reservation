from django.db import models


class Airline(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    origin_country = models.CharField(max_length=50, verbose_name='Origin Country')
    details = models.TextField(default='AirLine')


class Airplane(models.Model):
    manufacturer = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    register_number = models.BigIntegerField(verbose_name='Register Number', unique=True)
    number_of_seats = models.IntegerField(verbose_name='Number Of Seats')


class Airport(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

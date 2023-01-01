from rest_framework.serializers import ModelSerializer

from .models import *


class ResidentialCategorySerializer(ModelSerializer):
    class Meta:
        model = ResidentialCategory
        fields = ['id', 'title', 'is_valid']


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'star', 'name', 'about', 'country', 'state', 'city_or_section', 'number_of_rooms', 'capacity']


class HotelRoomSerializer(ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = ['id', 'hotel', 'room_number', 'floor', 'area', 'single_beds', 'double_beds', 'extra_beds',
                  'price_per_night']


class ResidentialSerializer(ModelSerializer):
    class Meta:
        model = Residential
        fields = ['id', 'price_per_night', 'name', 'about', 'country', 'state', 'city_or_section', 'number_of_rooms',
                  'floors', 'capacity', 'area']

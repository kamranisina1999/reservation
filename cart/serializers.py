from .models import UserCart
from rest_framework.serializers import ModelSerializer


class UserCartSerializer(ModelSerializer):
    class Meta:
        model = UserCart
        fields = ['user', 'cart_number', 'hotel_room_reservations', 'residential_reservations',
                  'flight_ticket_reservation', 'is_payed']

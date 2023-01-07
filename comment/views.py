from django.shortcuts import render

from booking.abstract.permissions import *
from rest_framework.generics import ListCreateAPIView
from .serializers import *


class HotelCommentView(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = HotelCommentSerializer

    def get_queryset(self):
        name = self.kwargs['hotel']
        return HotelComment.objects.filter(hotel__name=name, status='Approved').all()


class HotelRoomCommentView(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = HotelRoomCommentSerializer

    def get_queryset(self):
        id = self.kwargs['hotel_room_id']
        return HotelRoomComment.objects.filter(hotel_room__id=id, status='Approved').all()


class ResidentialCommentView(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ResidentialCommentSerializer

    def get_queryset(self):
        name = self.kwargs['residential']
        return ResidentialComment.objects.filter(residential__name=name, status='Approved').all()


class AirlineCommentView(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AirlineCommentSerializer

    def get_queryset(self):
        name = self.kwargs['airline']
        return AirLineComment.objects.filter(airline__name=name, status='Approved').all()


class AirportCommentView(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AirportCommentSerializer

    def get_queryset(self):
        name = self.kwargs['airport']
        return AirPortComment.objects.filter(airport__name=name, status='Approved').all()
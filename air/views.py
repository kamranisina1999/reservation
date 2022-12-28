from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from .serializers import *


class AirLinesDisplay(ListAPIView):
    queryset = Airline.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AirlineSerializer


class AirplaneDisplay(ListAPIView):
    queryset = Airplane.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AirplaneSerializer


class AirportDisplay(ListAPIView):
    queryset = Airport.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AirportSerializer

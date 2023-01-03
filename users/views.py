from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView
from abstract.permissions import IsOwner
from .serializers import ProfileSerializer
from .models import *


class ProfileDisplay(RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Profile.objects.filter(user=username).get()

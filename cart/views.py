from django.shortcuts import render
from booking.abstract.permissions import IsOwner
from .serializers import UserCartSerializer
from .models import UserCart
from rest_framework.generics import RetrieveAPIView


class UserCartDisplay(RetrieveAPIView):
    permission_classes = [IsOwner]
    serializer_class = UserCartSerializer

    def get_queryset(self):
        username = self.kwargs['user']
        return UserCart.objects.filter(UserCart__user__username=username).get()

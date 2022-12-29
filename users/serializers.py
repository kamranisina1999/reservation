from rest_framework.serializers import ModelSerializer
from .models import *


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'email', 'name', 'birthday', 'nationality', 'id_number', 'created_time']

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models.manager import BaseManager


class User(AbstractUser):
    phone_number = models.PositiveBigIntegerField(unique=True, null=True, blank=True,validators=[
        RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid ''phone number.', 'invalid')])
    is_anonymous = models.BooleanField(default=True)
    is_authenticated = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    avatar = models.ImageField()
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=100)

    birthday = models.DateField(null=True, blank=True, verbose_name='Date Of Birth')
    nationality = models.CharField(max_length=60, null=True, blank=True)
    id_number = models.PositiveIntegerField(default=111111)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    unique_together = ['nationality', 'id_number']

    def __str__(self):
        return self.user.username


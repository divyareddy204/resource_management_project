from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, null=True, unique=True)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(max_length=10, null=True, blank=True)

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    phone = models.CharField(blank=True, null=True, max_length=100)
    email=models.EmailField(null=True)
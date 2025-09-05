from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

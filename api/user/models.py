from django.db import models
# about the Django User model : https://docs.djangoproject.com/en/4.2/ref/contrib/auth/#django.contrib.auth.models.User
# 👇👇 AbstractUser helps in creating a user, and customised fields besides the default fields, and modify the default ones too
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default="Anonymous")
    email = models.EmailField(max_length=250, unique=True)
    
    # 👇👇 To require email and not the username while sign_up/log_in authorisation
    # For customised user model : https://docs.djangoproject.com/en/4.2/topics/auth/customizing/
    username = None
    USERNAME_FIELD = 'email'
    # 👇👇 For more on REQUIRED_FIELDS : https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
    REQUIRED_FIELDS = []
    
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    session_token = models.CharField(max_length=20, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings
from datetime import datetime


USER_TYPE = (
    ('Applicant', 'Applicant'),
    ('Employer', 'Employer'),
)

GENDER_SELECTION = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

LANGUAGES= (
    ('en', 'en'),
    ('ru', 'ru'),
    ('uz', 'uz'),
)

class CustomUser(AbstractUser):
    user_type= models.CharField(max_length=20, choices=USER_TYPE)
    phone = models.CharField(max_length=17, blank=True, null=True)
    telegram = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    linkedin= models.CharField(max_length=150, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    github = models.CharField(max_length=150, blank=True, null=True)
    youtube = models.CharField(max_length=150, blank=True, null=True)
    about = models.TextField(blank=True)
    languages = models.CharField(max_length=20, choices=LANGUAGES, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return str(self.username)
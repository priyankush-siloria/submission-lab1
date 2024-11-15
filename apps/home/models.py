from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Model for Company


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# User Profile model with many-to-one relationship with User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
    default_language = models.CharField(
        max_length=10,
        choices=[('en', 'English'), ('fr', 'French'),
                 ('es', 'Spanish'), ('it', 'Italian')],
        default='en'
    )

    def __str__(self):
        return self.user.username

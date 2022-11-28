from django.db import models
from authentication.models import User

# Create your models here.

class BookerProfile(models.Model):
    
    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    user = models.OneToOneField(
        User,
        default=User,
        verbose_name="User",
        on_delete=models.CASCADE,
        related_name='bookerprofile', null=False)
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    gender = models.CharField(choices=gender_choice, max_length=10)
from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import User
from .models import RiderProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.role == 2:
        RiderProfile.objects.create(user=instance)
    else:
        pass
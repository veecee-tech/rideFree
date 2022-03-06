from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import User
from .models import BookerProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.role == 3:
        BookerProfile.objects.create(user=instance)
    else:
        pass
from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import User
from .models import SourceDestination, Source, Destination,Orders
import uuid

@receiver(post_save, sender=SourceDestination)
def create_profile(sender, instance, created, **kwargs):

    qs = Source.objects.filter(name=instance.source)
    qr = Destination.objects.filter(name=instance.destination)
    if created:
        
        if qs.exists():
            pass
        else:
            Source.objects.create(name=instance.source)
        if qr.exists():
            pass
        else:
            Destination.objects.create(name=instance.destination)
        
    else:
        pass


@receiver(post_save, sender=Orders)
def generate_booking_id(sender,instance,created, **kwargs):

    if created:
        instance.booking_id = str(uuid.uuid4()).replace("-","")[:6]

        instance.save()
    else:
        pass
from django.db import models
from authentication.models import User
from django.utils import timezone
# Create your models here.


class SourceDestination(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.source} - {self.destination}"
    

class Source(models.Model):
    name = models.CharField(max_length=50,unique=True, editable=False)
    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=50,unique=True, editable=False)
    def __str__(self):
        return self.name
    

class Orders(models.Model):
    

    ORDER_CHOICES = (
        ('pending', 'pending'),
        ('received', 'received'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled')
    )

    booking_id = models.CharField(max_length=6, blank=True, null=True, unique=True)
    booker = models.ForeignKey(User, related_name='booker', on_delete = models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    pick_up_time = models.TimeField(auto_now=False, auto_now_add=False)
    pick_up_date = models.DateField(auto_now=False, auto_now_add=False)
    address = models.TextField(max_length=50)
    order_status = models.CharField(choices=ORDER_CHOICES, default='pending', max_length=50)
    payed = models.BooleanField(default=False, null=True, blank=True)
    rider = models.ForeignKey(User, related_name='rider', on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.booking_id
    
    




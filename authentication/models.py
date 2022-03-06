from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from .manager import UserManager

class User(AbstractBaseUser):

    USER_TYPE_CHOICES = (
      (1, 'admin'),
      (2, 'rider'),
      (3, 'booker'),
  )

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    phone = PhoneNumberField()

    #required
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    # is_rider = models.BooleanField(default=False)
    # is_booker = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'email',]

    objects = UserManager()

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True



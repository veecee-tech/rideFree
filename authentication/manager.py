from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self,username, phone, email, password=None):

        if username is None:
            raise ValueError("users Should Have a username")

        if email is None:
            raise ValueError("users Should Have an email")
        
        user = self.model(username=username, phone=phone, email=self.normalize_email(email))

        user.role = 3
        user.is_staff = True
        user.is_active = True
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, email=None, phone=None, password=None):
    
        if password is None:
            raise ValueError("password should not be none")

        user = self.create_user(username=username, email=email,phone=phone, password=password)

        user.is_superadmin= True
        user.is_staff = True
        user.is_admin = True
        user.role = 1
        user.is_active = True
        
        user.save(using=self._db)
        return user

        
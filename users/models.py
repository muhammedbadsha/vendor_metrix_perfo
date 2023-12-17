from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):

    username = models.CharField(max_length=30, unique=True)
    # Add other fields as needed

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
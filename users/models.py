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



class CustomUserToken(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)  # Example field for the token

    def __str__(self):
        return self.user.username
    


# class Product(models.Model):
#     product_name = models.CharField(max_length=255,null=True, blank=True)
#     product_price = models.CharField(max_length=255,null=True, blank=True)
#     def __str__(self) -> str:
#         return self.product_name
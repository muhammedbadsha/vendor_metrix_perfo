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
    def create_superuser(self, username, password=None, **extra_kwargs):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.create_user(username, password, **extra_kwargs)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):

    # name = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=30, unique=True,null=True,default=None)
    # Add other fields as needed
    objects = CustomUserManager()

    is_staff = models.BooleanField(default=False,null=True)
    is_active = models.BooleanField(default=True,null=True)
    is_admin = models.BooleanField(default=False,null=True)



    def __str__(self):
        return self.username
    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["password"]


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff_property(self):
        return self.is_staff
class CustomUserToken(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)  # Example field for the token



# class Product(models.Model):
#     product_name = models.CharField(max_length=255,null=True, blank=True)
#     product_price = models.CharField(max_length=255,null=True, blank=True)
#     def __str__(self) -> str:
#         return self.product_name
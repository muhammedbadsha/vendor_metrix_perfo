from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import CustomUser, CustomUserToken
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUserToken)
admin.site.register(CustomUser)



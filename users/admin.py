from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import CustomUser, CustomUserToken

admin.site.register(CustomUserToken)
admin.site.register(CustomUser)



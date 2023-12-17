from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.core.

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def authenticate(self,validated_data):
        username = validated_data['username']
        password = validated_data['password']
        
        user = CustomUser.objects.get(username=username,password=password)
        if user is not None:
            
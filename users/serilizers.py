from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
            model = CustomUser
            fields = ['username','password']


# class CreateProductSerializer(serializers.ModelSerializer):
#      class Meta:
          
#           model = Product
#           fields = ['product_name','product_price']
    
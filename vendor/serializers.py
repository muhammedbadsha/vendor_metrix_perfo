from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Vendor
import uuid,random

class RegisterSerializer(serializers.ModelSerializer):
    # vendor_code = serializers.UUIDField(default=uuid.uuid4())
    class Meta:
        model = Vendor
        fields = '__all__'

    def create(self, validated_data):
        vendor_code = str(uuid.uuid4())
        validated_data['vendor_code'] = vendor_code  # Add vendor_code to validated_data
        return super().create(validated_data)
        # fields = ['name', 'contact_details', 'address', 'vendor_code','on_time_delivery_rate','quality_rating_avg','avarage_response_time','fulfillment_rate']

    def update(self, instance, validated_data):


        return super().update(instance, validated_data)
# from django.contrib.auth.models import Group, User
# from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
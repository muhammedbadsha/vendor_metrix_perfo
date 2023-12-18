from rest_framework import serializers
from .models import OrderProduct
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# class OrderProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderProduct
#         fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'

    def update(self, instance, validated_data):
        # Specify the fields that can be updated
        fields_to_update = ['vendor', 'delivery_date', 'status', 'quality_rating']

        # Update only the specified fields
        for field in fields_to_update:
            if field in validated_data:
                setattr(instance, field, validated_data[field])

        # Save the updated instance
        instance.save()

        return instance

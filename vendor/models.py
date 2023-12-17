from django.db import models
import uuid,random

# Create your models here.




class Vendor(models.Model):
    name = models.CharField(max_length=200,null=True)
    contact_details_phone = models.TextField(max_length=16,null=True)
    address = models.CharField(max_length=1000)
    vendor_code = models.UUIDField(unique=True,null=True)
    on_time_delivery_rate = models.FloatField(null=False,default=0.0)
    quality_rating_avg = models.FloatField()
    avarage_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self) -> str:
        return self.name

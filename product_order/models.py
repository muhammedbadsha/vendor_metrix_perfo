from django.db import models
from vendor.models import Vendor
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

status_choices = (
    ('pending','pending'),
    ('completed','completed'),
    ('canceled','canceled')
)

class OrderProduct(models.Model):
    po_number = models.UUIDField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor,on_delete = models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    order_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices = status_choices)
    quality_rating = models.FloatField(
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=10)
        ],
        null=True,
        blank=True
        )
    issue_date = models.DateTimeField(null=True, blank=True)
    acknowledge_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.po_number
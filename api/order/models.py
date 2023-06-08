from django.db import models
from api.user.models import CustomUser

# Create your models here.
# https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    
    transaction_id = models.CharField(max_length=150, default=0)
    total_amount = models.FloatField(null=True, blank=True, default=0.0)
    products = models.CharField(max_length=1000)
    total_products = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
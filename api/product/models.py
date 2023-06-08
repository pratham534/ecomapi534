from django.db import models
from api.category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price = models.FloatField(blank=True, null=True, default=0.0)
    rating = models.FloatField(blank=True, null=True, default=0.0)
    instock = models.BooleanField(default=True)
    # 👇👇 syntax of image field
    dispic = models.ImageField(upload_to='images/', blank=True, null=True)
    # 👇👇 syntax for foreign key value
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
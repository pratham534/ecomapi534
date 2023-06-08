from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types

class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=550)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #👇👇 a function that determines the title of the each entry displayed in django-admin-panel
    def __str__(self):
        return self.name
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        # 👇👇 choosing which selective fields has to be serialized(**serialized => accessing the data as format which could be converted to XML or JSON format)(sent as API)
        fields = ('name', 'desc')
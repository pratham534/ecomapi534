from rest_framework import serializers
from .models import Product

# 👇👇 HyperlinkedModelSerializer does not include id field by default, rather a url field. incase of url of images, using ModelSerializer may result in incomplete url, which prevent images to be rendered
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # https://www.django-rest-framework.org/api-guide/fields/#imagefield
        dispic = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
        model = Product
        # 👇👇 which selective fields has to be serialized
        fields = ('id', 'name', 'desc', 'dispic', 'price', 'rating', 'category')
from rest_framework import serializers
from .models import Order

# 👇👇 HyperlinkedModelSerializer does not include id field by default, rather a url field. incase of url of images, using ModelSerializer may result in incomplete url, which prevent images to be rendered
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        # 👇👇 which selective fields has to be serialized(sent as API)
        fields = ('user','products','total_amount')
from rest_framework import serializers
from .models import Product
# title - CharField
# description - CharField
# price - DecimalField
# inventory_quantity - IntegerField

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'inventory_quantity']
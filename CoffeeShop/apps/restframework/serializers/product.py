from rest_framework import serializers
from ..models import Category, ProductCustomization, Product
from django.contrib.auth.hashers import make_password


class CategorySerializer(serializers.ModelSerializer):
    """
        Serialize MyUser Model into JSON field
    """

    class Meta(object):
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCustomizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCustomization
        fields = '__all__'

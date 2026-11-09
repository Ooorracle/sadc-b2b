from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "parent"]

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    business_name = serializers.CharField(source="business.name", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "business",
            "business_name",
            "category",
            "category_name",
            "name",
            "sku",
            "description",
            "base_price",
            "currency",
            "stock_status",
            "unit",
            "image",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "business", "created_at"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'slug']
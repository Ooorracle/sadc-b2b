from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "parent"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name", 
        "business", 
        "category", 
        "base_price", 
        "currency", 
        "stock_status", 
        "is_active"
    ]
    list_filter = ["category", "stock_status", "is_active", "currency"]
    search_fields = ["name", "sku", "business__name"]
    autocomplete_fields = ["business"]
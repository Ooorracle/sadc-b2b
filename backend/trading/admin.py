from django.contrib import admin
from .models import RFQ, Offer, Order

@admin.register(RFQ)
class RFQAdmin(admin.ModelAdmin):
    list_display = ["id", "retailer", "wholesaler", "product", "quantity", "status", "created_at"]
    list_filter = ["status", "created_at"]

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ["id", "rfq", "unit_price", "total_price", "currency", "status", "valid_until"]
    list_filter = ["status", "currency"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "retailer", "wholesaler", "total_amount", "currency", "status", "created_at"]
    list_filter = ["status", "currency", "created_at"]

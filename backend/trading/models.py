from django.db import models
from django.conf import settings
from businesses.models import Business
from catalogue.models import Product

class RFQ(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        RESPONDED = "RESPONDED", "Responded"
        ACCEPTED = "ACCEPTED", "Accepted"
        CANCELLED = "CANCELLED", "Cancelled"

    retailer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="rfqs"
    )
    id = models.BigAutoField(primary_key=True) 
    wholesaler = models.ForeignKey(
        Business, 
        on_delete=models.CASCADE, 
        related_name="received_rfqs"
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name="rfqs"
    )
    quantity = models.PositiveIntegerField()
    message = models.TextField(blank=True, help_text="Specific requirements or notes")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"RFQ #{self.id} - {self.product.name} by {self.retailer.username}"


class Offer(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending Review"
        ACCEPTED = "ACCEPTED", "Accepted"
        REJECTED = "REJECTED", "Rejected"
        EXPIRED = "EXPIRED", "Expired"

    rfq = models.OneToOneField(RFQ, on_delete=models.CASCADE, related_name="offer")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    valid_until = models.DateTimeField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Offer for RFQ #{self.rfq.id} - {self.total_price} {self.currency}"


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending Payment"
        PAID = "PAID", "Paid"
        PROCESSING = "PROCESSING", "Processing"
        SHIPPED = "SHIPPED", "Shipped"
        DELIVERED = "DELIVERED", "Delivered"
        CANCELLED = "CANCELLED", "Cancelled"

    retailer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        related_name="orders"
    )
    wholesaler = models.ForeignKey(
        Business, 
        on_delete=models.PROTECT, 
        related_name="sales_orders"
    )
    offer = models.OneToOneField(Offer, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    delivery_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.id} - {self.retailer.username}"
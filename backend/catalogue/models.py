from django.db import models
from django.utils.text import slugify
from businesses.models import Business

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, help_text="Brief description of the category")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='subcategories'
    )

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    class StockStatus(models.TextChoices):
        IN_STOCK = "IN_STOCK", "In Stock"
        LOW_STOCK = "LOW_STOCK", "Low Stock"
        OUT_OF_STOCK = "OUT_OF_STOCK", "Out of Stock"

    # Link to the Business (Wholesaler)
    business = models.ForeignKey(
        Business, 
        on_delete=models.CASCADE, 
        related_name="products"
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT, 
        related_name="products"
    )
    
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    # Pricing & Inventory
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    stock_status = models.CharField(
        max_length=20,
        choices=StockStatus.choices,
        default=StockStatus.IN_STOCK
    )
    unit = models.CharField(max_length=50, help_text="e.g., box, pallet, kg")
    
    # Media
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        # A business cannot have duplicate SKUs
        constraints = [
            models.UniqueConstraint(
                fields=['business', 'sku'], 
                name='unique_business_sku'
            )
        ]

    def __str__(self):
        return f"{self.name} - {self.business.name}"
from django.urls import path
from .views import (
    ProductListAPIView, 
    WholesalerProductListAPIView,
    BulkProductUploadAPIView,
    CategoryListAPIView  # Import the new view
)

app_name = "catalogue"

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="product-list"),
    path("categories/", CategoryListAPIView.as_view(), name="category-list"), # NEW ROUTE
    path("manage/", WholesalerProductListAPIView.as_view(), name="manage-products"),
    path("upload/<int:business_id>/", BulkProductUploadAPIView.as_view(), name="bulk-upload"),
]
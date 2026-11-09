from rest_framework import generics, filters, permissions
from .models import Product
from .serializers import ProductSerializer
from businesses.models import Business
import pandas as pd
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from businesses.models import Business
from .models import Product, Category
from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer 

class ProductListAPIView(generics.ListAPIView):
    """ 
    Public endpoint for retailers to browse and search the catalogue.
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # FR-06: Keyword search
    search_fields = ['name', 'description', 'business__name', 'category__name']
    ordering_fields = ['base_price', 'created_at']

    def get_queryset(self):
        # Only show active products from VERIFIED businesses
        return Product.objects.filter(
            is_active=True, 
            business__verification_status=Business.VerificationStatus.VERIFIED
        )

class WholesalerProductListAPIView(generics.ListCreateAPIView):
    """
    Private endpoint for wholesalers to manage their own products.
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return products belonging to the logged-in user's businesses
        return Product.objects.filter(business__owner=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the product to the user's business
        business_id = self.request.data.get("business_id") # type: ignore
        
        try:
            business = Business.objects.get(id=business_id, owner=self.request.user)
        except Business.DoesNotExist:
            raise permissions.ValidationError("Invalid business or unauthorized.") # type: ignore
            
        serializer.save(business=business)


class BulkProductUploadAPIView(APIView):
    """ 
    FR-05: Bulk CSV Import for Wholesalers.
    """
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request, business_id):
        # 1. Verify the user owns this business
        try:
            business = Business.objects.get(id=business_id, owner=request.user)
        except Business.DoesNotExist:
            return Response({"error": "Business not found or unauthorized."}, status=status.HTTP_403_FORBIDDEN)

        file = request.FILES.get('file')
        if not file or not file.name.endswith('.csv'):
            return Response({"error": "Please upload a valid CSV file."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 2. Read the CSV file using pandas
            df = pd.read_csv(file)
            
            # Validate required columns
            required_cols = ['name', 'sku', 'category', 'base_price', 'unit']
            missing_cols = [col for col in required_cols if col not in df.columns]
            if missing_cols:
                return Response({"error": f"Missing required columns: {', '.join(missing_cols)}"}, status=400)

            success_count = 0
            errors = []

            # 3. Loop through the rows and create products
            for index, row in df.iterrows():
                try:
                    # Get or create the category
                    category_name = str(row['category']).strip()
                    category, _ = Category.objects.get_or_create(name=category_name)
                    
                    # Create or update the product
                    Product.objects.update_or_create(
                        business=business,
                        sku=str(row['sku']).strip(),
                        defaults={
                            'category': category,
                            'name': str(row['name']).strip(),
                            'base_price': row['base_price'],
                            'currency': row.get('currency', 'USD'),
                            'unit': str(row['unit']).strip(),
                            'stock_status': row.get('stock_status', Product.StockStatus.IN_STOCK),
                            'description': row.get('description', '')
                        }
                    )
                    success_count += 1
                except Exception as e:
                    # Record the specific row error and continue
                    errors.append(f"Row {index + 2}: {str(e)}") # type: ignore

            return Response({
                "message": f"Import complete. {success_count} products processed.",
                "errors": errors
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Failed to process file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)




class CategoryListAPIView(generics.ListAPIView):
    """
    Public endpoint to list all available categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
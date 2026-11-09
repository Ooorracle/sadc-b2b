from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import RFQ, Offer, Order
from .serializers import RFQSerializer, OfferSerializer, OrderSerializer

class RFQListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RFQSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # If user has a business, show RFQs they received. Otherwise, show RFQs they sent.
        if hasattr(user, "owned_businesses"):
            return RFQ.objects.filter(wholesaler__owner=user)
        return RFQ.objects.filter(retailer=user)

    def perform_create(self, serializer):
        serializer.save(retailer=self.request.user)


class OfferCreateAPIView(generics.CreateAPIView):
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        rfq_id = self.kwargs.get("rfq_id")
        rfq = get_object_or_404(RFQ, id=rfq_id, wholesaler__owner=self.request.user)
        serializer.save(rfq=rfq)


class AcceptOfferAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, offer_id):
        # 1. Fetch the offer and ensure it belongs to the logged-in retailer
        offer = get_object_or_404(
            Offer, 
            id=offer_id, 
            rfq__retailer=request.user, 
            status=Offer.Status.PENDING
        )

        # 2. Check if it has expired
        from django.utils import timezone
        if offer.valid_until < timezone.now():
            offer.status = Offer.Status.EXPIRED
            offer.save()
            return Response({"error": "This offer has expired."}, status=status.HTTP_400_BAD_REQUEST)

        # 3. Update statuses
        offer.status = Offer.Status.ACCEPTED
        offer.save()
        
        offer.rfq.status = RFQ.Status.ACCEPTED
        offer.rfq.save()

        # 4. Create the Order
        delivery_address = request.data.get("delivery_address", "Default Address")
        
        order = Order.objects.create(
            retailer=request.user,
            wholesaler=offer.rfq.wholesaler,
            offer=offer,
            total_amount=offer.total_price,
            currency=offer.currency,
            delivery_address=delivery_address
        )

        return Response(
            {"message": "Offer accepted and order created successfully.", "order_id": order.id},
            status=status.HTTP_201_CREATED
        )
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from trading.models import Order
from .models import PaymentTransaction, DigitalReceipt
from .serializers import PaymentTransactionSerializer

class InitiatePaymentAPIView(generics.CreateAPIView):
    serializer_class = PaymentTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):
        # 1. Ensure the order exists and belongs to the logged-in retailer
        order = get_object_or_404(Order, id=order_id, retailer=request.user)

        # 2. Check if payment already exists
        if hasattr(order, 'payment'):
            return Response(
                {"error": "Payment already initiated for this order."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        payment_method = request.data.get("payment_method", "MANUAL")

        # 3. Create the abstract payment transaction
        payment = PaymentTransaction.objects.create(
            order=order,
            amount=order.total_amount,
            currency=order.currency,
            payment_method=payment_method,
            status=PaymentTransaction.Status.PENDING
        )

        # 4. SIMULATE GATEWAY CALLBACK (For MVP testing)
        # In production, this is where you redirect to Stripe/PayNow.
        # We will simulate a successful payment instantly for testing.
        payment.status = PaymentTransaction.Status.SUCCESSFUL
        payment.provider_reference = "SIMULATED-TXN-12345"
        payment.save()

        # 5. Update Order Status
        order.status = Order.Status.PAID
        order.save()

        # 6. Generate Digital Receipt
        DigitalReceipt.objects.create(
            payment=payment,
            qr_verification_url=f"https://sadcb2b.com/verify/{payment.provider_reference}"
        )

        return Response(
            PaymentTransactionSerializer(payment).data,
            status=status.HTTP_201_CREATED
        )

class MyReceiptsAPIView(generics.ListAPIView):
    """ Retrieves all digital receipts for the logged-in retailer """
    serializer_class = PaymentTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PaymentTransaction.objects.filter(
            order__retailer=self.request.user,
            status=PaymentTransaction.Status.SUCCESSFUL
        )
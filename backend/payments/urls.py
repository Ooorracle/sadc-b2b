from django.urls import path
from .views import InitiatePaymentAPIView, MyReceiptsAPIView

app_name = "payments"

urlpatterns = [
    path("initiate/<int:order_id>/", InitiatePaymentAPIView.as_view(), name="initiate-payment"),
    path("my-receipts/", MyReceiptsAPIView.as_view(), name="my-receipts"),
]
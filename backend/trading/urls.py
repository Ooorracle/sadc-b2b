from django.urls import path
from .views import (
    RFQListCreateAPIView, 
    OfferCreateAPIView, 
    AcceptOfferAPIView
)

app_name = "trading"

urlpatterns = [
    path("rfqs/", RFQListCreateAPIView.as_view(), name="rfq-list-create"),
    path("rfqs/<int:rfq_id>/offer/", OfferCreateAPIView.as_view(), name="offer-create"),
    path("offers/<int:offer_id>/accept/", AcceptOfferAPIView.as_view(), name="offer-accept"),
]
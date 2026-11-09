from django.urls import path
from .views import BusinessRegistrationAPIView, MyBusinessesAPIView

app_name = "businesses"

urlpatterns = [
    path("register/", BusinessRegistrationAPIView.as_view(), name="business-register"),
    path("my-businesses/", MyBusinessesAPIView.as_view(), name="my-businesses"),
]
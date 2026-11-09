from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Account registration
    path("api/accounts/", include("accounts.urls")),
    path("api/businesses/", include("businesses.urls")),
    path("api/catalogue/", include("catalogue.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/trading/", include("trading.urls")),
    path("api/communications/", include("communications.urls")),
    path("api/admin-dashboard/", include("marketplace_admin.urls")),
    
    # JWT token refresh
    path(
        "api/accounts/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
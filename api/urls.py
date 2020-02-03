from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('v1/auth/', include('accounts.urls')),
    path('v1/auth/', include('rest_auth.urls')),
    path('v1/auth/registration/', include('rest_auth.registration.urls')),
    path("v1/", include('property_ads.urls'))
]
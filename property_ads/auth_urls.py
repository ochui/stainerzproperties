from django.urls import path
from property_ads.views import AuthUserAdListView, AdDetailAPIView

urlpatterns = [
    path('ads', AuthUserAdListView.as_view(), name='ads_list'),
    path("ads/<int:pk>", AdDetailAPIView.as_view(), name='ads_detail'),
]

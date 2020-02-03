from django.urls import path
from property_ads.views import CategoryListAPIView, AdListAPIView

urlpatterns = [
    path('categories', CategoryListAPIView.as_view(), name='category'),
    path('ads', AdListAPIView.as_view(), name='ads_list'),
]
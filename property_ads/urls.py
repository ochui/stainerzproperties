from django.urls import path
from property_ads.views import CategoryListAPIView, AdListAPIView
from accounts.views import SubscriptionListView

urlpatterns = [
    path('categories', CategoryListAPIView.as_view(), name='category'),
    path('ads', AdListAPIView.as_view(), name='ads_list'),
    path("subscription", SubscriptionListView.as_view(), name="sub_list")
]

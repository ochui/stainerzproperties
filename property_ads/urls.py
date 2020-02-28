from django.urls import path
from property_ads.views import CategoryListAPIView, AdListAPIView, AdDetailAPIView, UserListAPIView, UserDetailAPIView
from accounts.views import SubscriptionListView

urlpatterns = [
    path('categories', CategoryListAPIView.as_view(), name='category'),
    path('ads', AdListAPIView.as_view(), name='ads_list'),
    path("ads/<int:pk>", AdDetailAPIView.as_view(), name='ads_detail'),
    path('users', UserListAPIView.as_view(), name='user_list'),
    path("users/<int:pk>", UserDetailAPIView.as_view(), name='user_detail'),
    path("subscription", SubscriptionListView.as_view(), name="sub_list")
]

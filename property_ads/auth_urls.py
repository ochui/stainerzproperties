from django.urls import path
from property_ads.views import AuthUserAdListView

urlpatterns = [
    path('ads', AuthUserAdListView.as_view(), name='ads_list'),
]

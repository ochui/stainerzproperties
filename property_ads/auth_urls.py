from django.urls import path
from property_ads.views import AuthUserAdListView, AuthUserAdDetailView

urlpatterns = [
    path('ads', AuthUserAdListView.as_view(), name='ads_list'),
    path("ads/<int:pk>", AuthUserAdDetailView.as_view(), name='ads_detail'),
]

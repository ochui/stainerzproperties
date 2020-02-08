from django.urls import path, include
from accounts.views import SubscriptionListView

urlpatterns = [
    path("subscription", SubscriptionListView.as_view(), name="")
]

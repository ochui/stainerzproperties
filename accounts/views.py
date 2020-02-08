from rest_framework.generics import ListAPIView
from accounts.models import Subscription
from accounts.serializers import SubscriptionSerializer


class SubscriptionListView(ListAPIView):

    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.all()

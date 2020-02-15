from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from property_ads.models import Ad, Category
from property_ads.serializers import AdSerializer, CategorySerializer


class CategoryListAPIView(generics.ListAPIView):

    """
    List all categories
    """

    serializer_class = CategorySerializer
    filterset_fields = ['parent']

    def get_queryset(self):
        if self.request.GET.get('parent'):
            return Category.objects.all()
        return Category.objects.filter(
            parent__isnull=True
        )


class AdListAPIView(generics.ListAPIView):

    """
    Returns an array of published properties
    """

    serializer_class = AdSerializer
    filterset_fields = [
        'region', 'place', 'category', 'is_negotiable',
        'broker_fee', 'price'
    ]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Ad.objects.all().order_by('created')


class AuthUserAdListView(generics.ListCreateAPIView):

    """
    Returns an array of propertied published by the login user
    """

    serializer_class = AdSerializer
    filterset_fields = [
        'region', 'place', 'category', 'is_negotiable',
        'broker_fee', 'price'
    ]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Ad.objects.filter(agent=self.request.user)

        return Ad.objects.none()

    def perform_create(self, serializer):
        serializer.save(agent=self.request.user)

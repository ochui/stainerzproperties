from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from property_ads.models import Ad, AdImage, Category
from property_ads.serializers import AdSerializer, AdImageSerializer, CategorySerializer


class CategoryListAPIView(ListAPIView):

    serializer_class = CategorySerializer
    filterset_fields = ['parent']

    def get_queryset(self):
        if self.request.GET.get('parent'):
            return Category.objects.all()
        return Category.objects.filter(
            parent__isnull=True
        )


class AdListAPIView(ListAPIView):

    serializer_class = AdSerializer
    filterset_fields = [
        'region', 'place', 'category', 'is_negotiable',
        'broker_fee', 'price'
    ]

    def get_queryset(self):
        return Ad.objects.all()

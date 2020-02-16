from django.db.models import Q
from django_filters import rest_framework as filters
from property_ads.models import Ad


class AdFilter(filters.FilterSet):

    cat_or_sub = filters.NumberFilter(method='category_or_subcategory', label="Category or Subcategory")

    def category_or_subcategory(self, queryset, name, value):
        """
        filter queryset for category or subcategory
        """
        return queryset.filter(Q(category=value) | Q(subcategory=value))

    class Meta:
        model = Ad
        fields = [
            'region', 'place', 'category', 'is_negotiable',
            'broker_fee', 'price', 'cat_or_sub'
        ]

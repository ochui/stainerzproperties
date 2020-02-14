from django.contrib.auth import get_user_model
# from django.conf import settings
from rest_framework import serializers
from accounts.serializers import UserDetailsSerializer
from property_ads.models import (
    Ad, AdImage, Category, AdField
)
USERMODEL = get_user_model()


class AdManagerDetailsSerializer(UserDetailsSerializer):

    """
    converts user id to user details object
    """

    class Meta:
        model = USERMODEL
        fields = (
            'first_name', 'last_name', 'email', 'phone_number', 'gender',
        )


class AdFieldSerializer(serializers.ModelSerializer):

    """
    AdField serializer
    """

    class Meta:
        model = AdField
        fields = (
            'name', 'placeholder', 'position'
        )


class CategorySerializer(serializers.ModelSerializer):

    """Category Serializer"""

    fields = AdFieldSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'description', 'parent', 'fields'
        )


class AdImageSerializer(serializers.ModelSerializer):

    """
   AdImage Serializer 
    """

    class Meta:
        model = AdImage
        fields = (
            'id', 'image', 'position'
        )


class AdSerializer(serializers.ModelSerializer):

    """
    Property Serializer
    """

    images = AdImageSerializer(source='ad_set', many=True, read_only=True)

    class Meta:
        model = Ad
        fields = [
            "id", "title", "price_currency", "price",
            "is_negotiable", "broker_fee", "description", "attrs", "images",
            "address", "region", "place", "created", "updated", "agent", "category"
        ]

        read_only_fields = (
            'user',
        )

    def create(self, validated_data):

        images_data = self.context.get('view').request.FILES
        ad = super(AdSerializer, self).create(validated_data)
        for index, image_data in enumerate(images_data.values()):
            AdImage.objects.create(
                ad=ad, image=image_data, position=index)
        return ad

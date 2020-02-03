from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers
from accounts.serializers import UserDetailsSerializer
from property_ads.models import (
    Ad, AdImage, Category
)
UserModel = get_user_model()


class AdManagerDetailsSerializer(UserDetailsSerializer):

    class Meta:
        model = UserModel
        fields = (
            'first_name', 'last_name', 'email', 'phone_number', 'gender',
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            '__all__'
        )


class AdImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdImage
        fields = (
            'id', 'image', 'position'
        )


class AdSerializer(serializers.ModelSerializer):

    # images = UpdateSerializer(source='update_set', many=True, read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'

        # read_only_fields = (
        #     'expires', 'user'
        # )

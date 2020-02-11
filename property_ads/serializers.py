from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers
from accounts.serializers import UserDetailsSerializer
from property_ads.models import (
    Ad, AdImage, Category, AdField
)
UserModel = get_user_model()


class AdManagerDetailsSerializer(UserDetailsSerializer):

    class Meta:
        model = UserModel
        fields = (
            'first_name', 'last_name', 'email', 'phone_number', 'gender',
        )


class AdFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdField
        fields = (
            'name', 'placeholder', 'position'
        )


class CategorySerializer(serializers.ModelSerializer):

    fields = AdFieldSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'description', 'parent', 'fields'
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

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from rest_auth.registration.serializers import RegisterSerializer
from phonenumber_field.serializerfields import PhoneNumberField

UserModel = get_user_model()


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta:
        model = UserModel
        fields = (
            'pk', 'username', 'first_name', 'last_name', 'account_type',
            'email', 'phone_number', 'date_of_birth', 'gender', 'address',
            'city', 'state', 'bio'
        )
        read_only_fields = ('email', 'username')


class CustomRegisterSerializer(RegisterSerializer):

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = PhoneNumberField(required=True)

    def get_cleaned_data(self):
        data = super(CustomRegisterSerializer, self).get_cleaned_data()

        custom_data = {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone_number': self.validated_data.get('phone_number'),
        }

        return {**data, **custom_data}

    def custom_signup(self, request, user):

        user.phone_number = self.cleaned_data['phone_number']
        user.save()

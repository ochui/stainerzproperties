from django.contrib.auth import get_user_model
from rest_auth.serializers import UserDetailsSerializer

UserModel = get_user_model()


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta:
        model = UserModel
        fields = (
            'pk', 'username', 'first_name', 'last_name',
            'email', 'phone_number', 'date_of_birth', 'gender',
        )
        read_only_fields = ('email', 'username')

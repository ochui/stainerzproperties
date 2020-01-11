from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm, AddEmailForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    CustomUserCreationForm will be used from django admin site
    and is only available to staff users during user creation
    """

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    """
    CustomUserChangeForm will be used from django admin site
    and is only available to staff users during user update
    """
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'date_of_birth',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofill': False
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofill': False
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofill': False
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'autofill': False
                }
            )
        }

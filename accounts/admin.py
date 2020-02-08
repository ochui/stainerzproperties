from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Subscription


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'phone_number', 'account_type']
    list_filter = ['account_type', 'date_joined', 'last_login', 'is_active', 'is_staff']
    search_fields = ['username', 'email', 'phone_number']
    fieldsets = UserAdmin.fieldsets + (
        ('KYC', {'fields': ('phone_number', 'gender', 'date_of_birth')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('KYC', {'fields': ('phone_number', 'gender', 'date_of_birth')}),
    )
    
    model = CustomUser


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'price']

from django.contrib import admin
from .models import (
    Category, Ad, AdImage, AdField
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'parent']
    list_filter = ['name', 'parent']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    list_display = ['title', 'category', 'agent', 'region', 'place']
    list_display = ['category', 'region', 'place']


@admin.register(AdField)
class AdFieldAdmin(admin.ModelAdmin):

    list_display = ['name', 'placeholder', 'position']


@admin.register(AdImage)
class AdImageAdmin(admin.ModelAdmin):

    list_display = ['ad']

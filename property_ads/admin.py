from django.contrib import admin
from .models import (
    Category, Ad, AdImage
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'parent']
    list_filter = ['name', 'parent']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'category', 'agent', 'region', 'place']
    list_display = ['category', 'region', 'place']

from django.contrib import admin
from .models import Category, SubCategory, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "category")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "subcategory", "price", "is_active")
    list_filter = ("subcategory", "is_active")

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, SubCategory, Service


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }
    list_display = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }
    list_display = ("name", "category")
    list_filter = ("category",)


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ("title", "subcategory", "price", "is_active")
    list_filter = ("subcategory", "is_active")
    search_fields = ("title", "description")

admin.site.site_header = "Galaxy Motors Administration"
admin.site.site_title = "Galaxy Motors Admin"
admin.site.index_title = "Управление сервисом Galaxy Motors"
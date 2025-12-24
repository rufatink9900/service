from modeltranslation.translator import register, TranslationOptions
from .models import Category, SubCategory, Service


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("title", "description")

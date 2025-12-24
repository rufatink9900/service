from modeltranslation.translator import translator, TranslationOptions
from .models import Category, SubCategory, Service

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)


class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(SubCategory, SubCategoryTranslationOptions)


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Service, ServiceTranslationOptions)

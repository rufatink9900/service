from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    """
    Brand / Manufacturer (e.g. Changan, Tesla, BYD)
    """
    name = models.CharField(_("Name"), max_length=100, unique=True)
    slug = models.SlugField(_("Slug"), unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """
    Car Model (e.g. CS55 Plus, UNI-K)
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="models",
        verbose_name=_("Category")
    )
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"))

    class Meta:
        unique_together = ("category", "slug")
        verbose_name = _("SubCategory")
        verbose_name_plural = _("SubCategories")

    def __str__(self):
        return f"{self.category.name} — {self.name}"


class Service(models.Model):
    """
    Service item
    """
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="services",
        verbose_name=_("SubCategory")
    )

    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    photo = CloudinaryField(_("Service Image"))

    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(_("Is Active"), default=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.title

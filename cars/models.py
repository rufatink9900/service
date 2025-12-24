from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Brand / Manufacturer (e.g. Changan, Tesla, BYD)
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """
    Car Model (e.g. CS55 Plus, UNI-K)
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="models"
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        unique_together = ("category", "slug")

    def __str__(self):
        return f"{self.category.name} — {self.name}"


class Service(models.Model):
    """
    Service item
    """
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="services"
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = CloudinaryField("service_image")

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

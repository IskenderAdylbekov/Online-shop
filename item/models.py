from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse("items_by_category", args=[self.slug])

    class Meta:
        ordering = ["name"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="item_images/%Y/%m/%d", blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("detail", args=[self.id, self.slug])

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

from django.contrib import admin

from .models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_display_links = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "is_sold", "created_at"]
    list_filter = ["is_sold", "created_at"]
    list_editable = ["is_sold", "price"]
    prepopulated_fields = {"slug": ("name",)}

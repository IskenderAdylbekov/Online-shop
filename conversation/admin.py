from django.contrib import admin

from .models import Conversation, ConversationMessage


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ["item", "slug", "created_by"]
    list_display_links = ["item", "created_by"]
    list_filter = ["modified_at", "members"]
    prepopulated_fields = {"slug": ("item",)}


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ["conversation", "slug", "created_by", "created_at"]
    list_display_links = ["conversation", "slug", "created_by"]
    list_filter = ["conversation", "created_by"]
    prepopulated_fields = {"slug": ("conversation",)}

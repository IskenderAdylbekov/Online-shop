from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


from item.models import Item


class Conversation(models.Model):
    item = models.ForeignKey(
        Item, related_name="conversations", on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=200, blank=True, null=True)
    members = models.ManyToManyField(User, related_name="conversations")
    created_by = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-modified_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item.slug)
        super().save(*args, **kwargs)


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(
        Conversation, related_name="messages", on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=200, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="created_messages", on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.conversation.item.slug)
        super().save(*args, **kwargs)

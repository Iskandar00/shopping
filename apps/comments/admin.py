from django.contrib import admin

from apps.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'name', 'email', 'message', 'rating', 'created_at',)

    readonly_fields = ('product', 'user', 'name', 'email', 'message', 'rating', 'created_at',)

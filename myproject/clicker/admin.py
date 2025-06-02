from django.contrib import admin
from .models import ClickerImage, Comment, ChatMessage

@admin.register(ClickerImage)
class ClickerImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'click_count', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    readonly_fields = ('click_count',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'created_at')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('username', 'message', 'timestamp')
    list_filter = ('timestamp',)
    readonly_fields = ('timestamp',)
    list_per_page = 50
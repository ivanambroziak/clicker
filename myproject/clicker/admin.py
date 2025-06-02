from django.contrib import admin
from .models import ClickerImage, Comment

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

# clicker_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('click/', views.click_button, name='click_button'),
    path('add_comment/', views.add_comment, name='add_comment'),
]
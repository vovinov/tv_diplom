from django.contrib import admin

from core.apps.news.models.news import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at", "updated_at")

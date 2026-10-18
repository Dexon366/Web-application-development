from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product_name',
        'author',
        'rating',
        'useful_count',
        'created_at',
    )
    list_filter = ('rating', 'created_at')
    search_fields = ('product_name', 'author', 'text')
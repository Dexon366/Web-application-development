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

    list_display_links = ('product_name',)

    list_filter = (
        'rating',
        'created_at',
    )

    search_fields = (
        'product_name',
        'author',
        'text',
    )

    ordering = (
        '-created_at',
    )

    fieldsets = (
        (
            'Основная информация',
            {
                'fields': (
                    'product_name',
                    'author',
                    'rating',
                    'text',
                ),
            },
        ),
        (
            'Дополнительная информация',
            {
                'fields': (
                    'useful_count',
                    'image',
                ),
            },
        ),
        (
            'Дата создания',
            {
                'fields': (
                    'created_at',
                ),
            },
        ),
    )

    readonly_fields = (
        'created_at',
    )
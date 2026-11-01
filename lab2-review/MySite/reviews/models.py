from django.db import models


class Review(models.Model):
    product_name = models.CharField(
        max_length=200,
        verbose_name='Название товара',
    )
    author = models.CharField(
        max_length=100,
        verbose_name='Автор',
    )
    rating = models.IntegerField(
        verbose_name='Оценка',
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    useful_count = models.IntegerField(
        default=0,
        verbose_name='Количество отметок полезности',
    )
    image = models.ImageField(
        upload_to='reviews/',
        blank=True,
        verbose_name='Изображение товара',
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.product_name} — {self.author}'
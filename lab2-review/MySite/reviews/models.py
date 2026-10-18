from django.db import models


class Review(models.Model):
    product_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    useful_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product_name} — {self.author}'

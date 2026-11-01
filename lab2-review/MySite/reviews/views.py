from django.shortcuts import render

from .models import Review


def index(request):
    reviews = Review.objects.all()

    high_rated_reviews = Review.objects.filter(
        rating__gt=3,
    )

    context = {
        'reviews': reviews,
        'high_rated_reviews': high_rated_reviews,
    }

    return render(request, 'reviews/index.html', context)
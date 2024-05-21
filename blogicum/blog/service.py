from django.core.paginator import Paginator
from django.db.models import Count
from django.utils import timezone

from blog.constants import POSTS_ON_PAGE


def get_posts(post_objects):
    """Посты из БД."""
    return post_objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).annotate(comment_count=Count('comments'))


def get_paginator(request, items, num=POSTS_ON_PAGE):
    """Создает объект пагинации."""
    return Paginator(items, num).get_page(request.GET.get('page'))

from django.db.models import Count
from django.utils import timezone


def get_posts(post_objects):
    """Посты из БД."""
    return post_objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).annotate(comment_count=Count('comments'))

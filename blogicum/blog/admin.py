from django.contrib import admin

from .models import Category, Comment, Location, Post

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'category',
        'author',
        'location',
        'text',
        'pub_date',
        'created_at',
    )
    list_editable = (
        'is_published',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category', 'is_published',)
    list_display_links = ('title',)

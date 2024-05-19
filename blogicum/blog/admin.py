from django.contrib import admin

from .models import Location, Category, Comment, Post

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

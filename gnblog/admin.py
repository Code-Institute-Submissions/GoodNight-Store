from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'subtitle',
        'slug',
        'created',
        'author',
        'image',
        'image_url'
        )
    list_filter = ('created',)
    search_fields = ['title', 'subtitle', 'body']


admin.site.register(Post, PostAdmin)

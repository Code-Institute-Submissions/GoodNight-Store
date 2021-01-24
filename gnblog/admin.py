from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'postUrl','created', 'author')
    list_filter = ('status',)
    search_fields = ['title', 'subtitle', 'body']


admin.site.register(Post, PostAdmin)

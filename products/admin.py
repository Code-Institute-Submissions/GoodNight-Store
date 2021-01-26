from django.contrib import admin
from .models import Product, Category, ProductReview

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'image_url'
    )

    ordering = ('-sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'image',
        'name',
        'description',
    )

class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
        'rate',
        'added_on',
        'body',
        'email',
        'active',
        )
    list_filter = (
        'active',
        'added_on',
    )
    actions = ['approve_review', 'disaprove_review']

    def approve_review(self, request, queryset):
        queryset.update(active=True)

    def disaprove_review(self, request, queryset):
        queryset.update(active=False)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewsAdmin)

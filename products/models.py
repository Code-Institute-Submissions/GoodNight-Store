from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Category(models.Model):

    description = models.TextField(
        default="This is a text which describe category\
             and will be displayed in product page"
        )
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    sku = models.CharField(max_length=16, null=True, blank=True)
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def rating(self):
        try:
            all_rates = self.review.all()
            rate_dict = all_rates.aggregate(Avg('rate'))
            return round(rate_dict['rate__avg'], 2)
        except Exception as ex:
            return 'N/A'

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='review'
        )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.CharField(max_length=512)
    added_on = models.DateTimeField(auto_now=True)
    rate = models.DecimalField(
        max_digits=1,
        decimal_places=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['added_on']

    def __str__(self):
        return '{} reviewed this product \
            {} with {} star and comment: {}'.format(
            self.name, self.added_on, self.rate, self.body)

from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=256, unique=True, null=False, blank=False)
    subtitle = models.CharField(max_length=512, null=True, blank=True)
    body = models.TextField()
    postUrl = AutoSlugField(populate_from='title')
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="anonymous author")
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.title

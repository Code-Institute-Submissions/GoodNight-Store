from django import forms
from .models import Post
from products.widgets import CustomClearableFileInput

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

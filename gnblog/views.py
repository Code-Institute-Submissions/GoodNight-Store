from django.shortcuts import render
from .models import Post

def blog(request):
    """ A view to render gnblog.html template """
    post = Post.objects.filter(status=1).order_by('-created')
    context = {
        'post': post
    }

    return render(request, 'gnblog/blog.html', context)

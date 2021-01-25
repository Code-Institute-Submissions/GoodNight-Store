from django.shortcuts import render, redirect, reverse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogPostForm

def blog(request):
    """ A view to render gnblog.html template """
    post = Post.objects.filter(status=1).order_by('-created')
    context = {
        'post': post
    }

    return render(request, 'gnblog/blog.html', context)

@login_required
def add_post(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse ('home'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Succesfully added Post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid')
    else:
        form = BlogPostForm()

    template = 'gnblog/add_post.html'
    context = {
        'form': form
    }

    return render(request, template, context)

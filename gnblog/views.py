from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogPostForm

def blog(request):
    """ A view to render gnblog.html template """
    post = Post.objects.order_by('-created')
    context = {
        'post': post
    }

    return render(request, 'gnblog/blog.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'gnblog/post_detail.html', context)


@login_required
def add_post(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse ('home'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
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


@login_required
def edit_post(request, slug):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse ('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succesfully updated post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid')
    else:
        form = BlogPostForm(instance=post)
        messages.info(request, f'You are editing {post.title} post')

    template = 'gnblog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def remove_post(request, slug):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse ('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post removed!')
    return redirect(reverse('blog'))
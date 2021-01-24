from django.shortcuts import render


def blog(request):
    """ A view to render gnblog.html template """
    return render(request, 'gnblog/blog.html')

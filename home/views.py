from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to render index.html template """
    return render(request, 'home/index.html')
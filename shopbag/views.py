from django.shortcuts import render

# Create your views here.
def shopbag(request):
    """ A view to render index.html template """
    return render(request, 'shopbag/shopbag.html')

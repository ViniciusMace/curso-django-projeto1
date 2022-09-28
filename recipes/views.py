from django.shortcuts import render

# Create your views here.


# HTTP REQUEST
def home(request):
    return render(request, 'recipes/home.html')
    # return HTTP RESPONSE

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# HTTP REQUEST
def home(request):
    return render(request, 'recipes/home.html')
    # return HTTP RESPONSE


def sobre(request):
    return render(request, 'temp/temp.html')


def contato(request):
    return HttpResponse('CONTATO')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    context = {
        'mainModuleName': 'inicio',
        'defaultUrl':'dashboard',
    }

    # Page from the theme 
    return render(request, 'pages/dashboard.html', context=context)

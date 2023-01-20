import os
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello Django! Here is \"<a href=\"/rango/about\">about</a>\" page</h1>")
    content_text = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
    }

    return render(request, 'rango/index.html', content_text)

def about(request):
    # print(__file__)
    # print(os.path.dirname(__file__))
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # return HttpResponse("HttpResponse: 'Rango says here is the about page.' Now we can go \"<a href=\"/rango/index\">index</a>\" page")
    return render(request, 'rango/about.html')
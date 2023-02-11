import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Page
from .forms import CategoryForm

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello Django! Here is \"<a href=\"/rango/about\">about</a>\" page</h1>")
    content_text = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
    }

    category = Category.objects.order_by('id')

    content_text['category'] = category

    # return render(request, 'rango/index.html', content_text)
    return render(request, 'base/base.html', content_text)

def about(request):
    # print(__file__)
    # print(os.path.dirname(__file__))
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # return HttpResponse("HttpResponse: 'Rango says here is the about page.' Now we can go \"<a href=\"/rango/index\">index</a>\" page")
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return redirect('/rango/')

        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('about/', about),
    path('category/<slug:category_name_slug>', show_category, name = 'category')
]
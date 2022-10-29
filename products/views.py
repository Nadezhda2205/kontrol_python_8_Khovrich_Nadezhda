# from django.shortcuts import render
from django.views.generic import ListView


from products.models import Product


class ProductListView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'


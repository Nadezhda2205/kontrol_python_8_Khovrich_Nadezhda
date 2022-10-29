from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse

from products.models import Product


class ProductListView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name: str = 'products/product.html'
    model = Product
    context_object_name = 'product'


class ProductCreateView(CreateView):
    template_name: str = 'products/product_add.html'
    model = Product
    fields = ('name', 'description', 'image', 'category', 'description')
    
    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})


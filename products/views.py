from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

from products.models import Product, Comment
from products.forms import ProductForm, CommentForm
from accounts.models import Account


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ProductListView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    groups = ['Moderator']


class ProductDetailView(DetailView):
    template_name: str = 'products/product.html'
    model = Product
    context_object_name = 'product'
    groups = ['Moderator']


class ProductCreateView(CreateView):
    template_name: str = 'products/product_add.html'
    model = Product
    form_class = ProductForm
    groups = ['Moderator']

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})



class ProductUpdateView(UpdateView):
    template_name = 'products/product_edit.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'products'

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'products/product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    groups = ['Moderator']

    
class CommentListView(ListView):
    template_name = 'product.html'
    model = Comment
    context_object_name = 'comments'


class CommentCreateView(CreateView):
    template_name: str = 'comments/product_comment_add.html'
    model = Comment
    form_class = CommentForm
    
    def get_success_url(self):
        return reverse('index')


class CommentUpdateView(UpdateView):
    template_name = 'comments/comment_edit.html'
    form_class = CommentForm
    model = Comment
    context_object_name = 'comments'

    def get_success_url(self):
        return reverse('index')


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self, **kwargs):
        return reverse_lazy('product', kwargs={'pk': self.get_object().product.pk})


class UserPageView(ListView):
    template_name = 'user_page.html'
    model = Account
    context_object_name = 'user'



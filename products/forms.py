from django import forms
from products.models import Product, Comment
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'image']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'product', 'text', 'valuation']

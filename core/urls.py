
from django.contrib import admin
from django.urls import path
from accounts.views import  LoginView, logout_view, RegisterView
from products.views import (
    ProductListView, 
    ProductDetailView, 
    ProductCreateView, 
    ProductUpdateView, 
    ProductDeleteView, 
    CommentListView, 
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    
)
from accounts.views import UserPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product/confirm-delete/<int:pk>', ProductDeleteView.as_view(), name='product_confirm_delete'),
    

    path('product/comments/<int:pk>', CommentListView.as_view(), name='product_comments'),
    path('product/comment/<int:pk>/add', CommentCreateView.as_view(), name='product_comment_add'),
    path('product/<int:pk>/comment/edit', CommentUpdateView.as_view(), name='product_comment_edit'),
    path('product/comment/<int:pk>/delete', CommentDeleteView.as_view(), name='product_comment_delete'),

    path('user/<int:pk>', UserPageView.as_view(), name='user_page'),


    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),


    path('signup/', RegisterView.as_view(), name='signup'),
]

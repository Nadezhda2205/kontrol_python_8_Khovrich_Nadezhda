
from django.contrib import admin
from django.urls import path
from accounts.views import  LoginView, logout_view, RegisterView
from products.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, CommentListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product/confirm-delete/<int:pk>', ProductDeleteView.as_view(), name='product_confirm_delete'),
    
    path('product/comments/<int:pk>', CommentListView.as_view(), name='product_comments'),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('signup/', RegisterView.as_view(), name='signup'),
]

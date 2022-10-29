
from django.contrib import admin
from django.urls import path
from accounts.views import  LoginView, logout_view, RegisterView
from products.views import ProductListView, ProductDetailView, ProductCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('signup/', RegisterView.as_view(), name='signup'),
]


from django.contrib import admin
from django.urls import path
from accounts.views import  LoginView, logout_view, RegisterView
from products.views import ProductListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('signup/', RegisterView.as_view(), name='signup'),
]

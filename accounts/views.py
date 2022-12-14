
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth import authenticate, login, logout
from accounts.models import Account

from accounts.forms import CustomUserŠ”reationForm
from accounts.forms import LoginForm


class UserPageView(DetailView):
    template_name = 'user_page.html'
    model = Account
    context_object_name = 'user'


class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    form = LoginForm


    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')

        username: str = form.cleaned_data.get('username')
        password: str = form.cleaned_data.get('password')
        user = authenticate(request=request, username=username, password=password)

        if not user:
            return redirect('login')

        login(request, user)

        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')



class RegisterView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserŠ”reationForm
    succes_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)
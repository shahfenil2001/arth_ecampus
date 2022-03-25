from re import template
from sre_constants import SUCCESS
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from .forms import UserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from userapp.models import User

# Create your views here.

class BaseRegisterView(SuccessMessageMixin, FormView):
    model = User
    form_class = UserForm
    template_name = 'userportal/registration.html'
    success_url = '/user/user-login'

  
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password) 
        user.save()    
        return super().form_valid(form)

    # def get_success_message(self, cleaned_data):
    #     username = cleaned_data["username"]
    #     return username + " - User Created Successfully..!!"
    

class UserLoginView(LoginView):
    template_name = 'userportal/user_login.html'
    success_url ="/userapp/index/"

def index(request):
    return render(request, 'index.html')


class ViewUser(ListView):
    model = User
    users = model.objects.all()
    context_object_name = 'users'
    template_name = 'userportal/view_user.html'

class DetailUser(DetailView):
    model = User
    template_name = 'userportal/detail_user.html'
    context_object_name = 'user'

class DeleteUser(DeleteView):
    model = User
    template_name = 'userportal/delete_user.html'
    success_url = '/user/view'

class UpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'userportal/update_user.html'
    success_url = '/user/view'

class UserRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name ='userportal/user_signup.html'
    success_url = "userapp/index"

    
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, CreateUserForm
from django.contrib.auth.decorators import login_required


def homepage(request):
    # foods = Food.objects.all().order_by('-id')[:3]
    # context = {
    #     'foods': foods
    # }
    return render(request, 'account/homepage.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('/login')

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            print(user)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('/admins/dashboard')
                elif not user.is_staff:
                    login(request, user)
                    return redirect('/products/homepage')
            else:
                messages.add_message(request, messages.ERROR, "Invalid user credentials")
                return render(request, 'account/login.html', {'form_login':form})
    context={
        'form_login':LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'account/login.html', context)

def register_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.add_message(request, messages.SUCCESS, 'User Registered Successfully')
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, 'Unable To Register User')
            return render(request, 'account/register.html', {'form_register': form})
    context = {
        'form_register': CreateUserForm,
        'activate_register': 'active'
    }
    return render(request, 'account/register.html', context)

def add_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.add_message(request, messages.SUCCESS, 'User added Successfully')
            return redirect('/admins/users')
        else:
            messages.add_message(request, messages.ERROR, 'Unable To Register User')
            return render(request, 'account/add_user.html', {'form_register': form})
    context = {
        'form_register': CreateUserForm,
        'activate_register': 'active'
    }
    return render(request, 'account/add_user.html', context)


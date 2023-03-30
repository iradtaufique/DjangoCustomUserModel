from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from userAccount.forms import RegistrationForm, UserAuthenticationForm


def home(request):
    return render(request, 'base.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'user_account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('/')

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return redirect('/')
    else:
        form = UserAuthenticationForm()
    context['login_form'] = form
    return render(request, 'user_account/login.html', context)

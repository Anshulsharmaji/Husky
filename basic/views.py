#django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

#parent directory
from .forms import UserRegistrationForm

#request is a httprequestobject sent by the user

def index(request):
    if not request.user.is_authenticated():
        return redirect('basic:login')


def see_about(request):
    return render(request, "base/about.html")


def see_privacy(request):
    return render(request, "base/privacy.html")


def see_terms(request):
    return render(request, "base/terms.html")


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            return HttpResponseRedirect("/signup_success/")
    else:
        form = UserRegistrationForm()
    return render(request, "base/signup.html", {"form": form})


def login_user(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('basic:index')

    return render(request, 'base/login.html', {
        'form': form
    })


def signout(request):
    logout(request)
    return render(request, 'base/logged_out.html')


def signup_success(request):
    return render(request, 'base/signup_success.html')


from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    return redirect('/accounts/google/login')

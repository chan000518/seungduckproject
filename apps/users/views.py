from django.db import models

# Create your models here.
from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import CustomUserChangeForm
from .forms import userCreate
from django.contrib.auth.forms import AuthenticationForm
from .models import *
# Create your views here.

# 유저 프로필 페이지
def user_detail(request):
    user = request.user
    if user.is_authenticated:
        ctx = {
            'user' : user,
        }
        return render(request, 'users/user_detail.html', ctx)
    return redirect('users:login') #users:login = 로그인 페이지


# 유저 계정 탈퇴 페이지
def user_delete(request):
    user = request.user
    if user.is_authenticated:
        user.delete()
        auth.logout(request)
    return redirect('users:main') #users:main = 로그인 하기 전에 보여지는 main 페이지


# 유저 프로필 수정 페이지
def user_update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:user_detail')
    form = CustomUserChangeForm(instance=request.user)
    ctx = {
        'form' : form,
    }
    return render(request, 'users/user_update.html', ctx)

# 로그아웃
def user_logout(request):
    auth.logout(request)
    return redirect('users:main')


def signup(request):
    if request.method == 'POST':
        form = userCreate(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('users:main')
    else:
        form = userCreate()

    ctx = {'form': form}
    return render(request, 'users/user_signup.html', ctx)


def login (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('users:main')
        else:
            ctx = {
                'form' : form
            }
            return render(request, 'users/user_login.html', ctx)
    else:
        form = AuthenticationForm()
        ctx = {
            
            'form': form,
        }
        return render(request, 'users/user_login.html', ctx)
    
def logout(request):
    auth.logout(request)
    return redirect('users:main')

def main (request):
    users = User.objects.all()
    ctx = {
        'users' : users
    }
    return render(request, 'users/user_main.html', ctx)

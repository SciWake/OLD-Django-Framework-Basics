from django.shortcuts import render

from users.forms import UserLoginForm


def login(request):
    context = {
        'title': 'GeekShop - Авторизация',
        'form': UserLoginForm()
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {'title': 'GeekShop - Регистрация'}
    return render(request, 'users/register.html', context)

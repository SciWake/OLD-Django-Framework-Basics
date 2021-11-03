from django.shortcuts import render

from users.models import User


def index(request):
    context = {'title': 'GeekShop - Панель Администратора'}
    return render(request, 'my_admin/index.html', context)


def admin_users_create(request):
    context = {'title': 'GeekShop - Создание пользователей'}
    return render(request, 'my_admin/admin-users-create.html', context)


def admin_users(request):
    context = {'title': 'GeekShop - Пользователи', 'users': User.objects.all()}
    return render(request, 'my_admin/admin-users-read.html', context)


def admin_users_update(request):
    context = {'title': 'GeekShop - Обновление пользователя'}
    return render(request, 'my_admin/admin-users-update-delete.html', context)


def admin_users_delete(request):
    pass

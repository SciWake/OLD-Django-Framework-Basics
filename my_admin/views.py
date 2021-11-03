from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from my_admin.forms import UserAdminRegistrationForm


def index(request):
    context = {'title': 'GeekShop - Панель Администратора'}
    return render(request, 'my_admin/index.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_admin:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'Админ-панель - Создание пользователя', 'form': form}
    return render(request, 'my_admin/admin-users-create.html', context)


def admin_users(request):
    context = {'title': 'GeekShop - Пользователи', 'users': User.objects.all()}
    return render(request, 'my_admin/admin-users-read.html', context)


def admin_users_update(request):
    context = {'title': 'GeekShop - Обновление пользователя'}
    return render(request, 'my_admin/admin-users-update-delete.html', context)


def admin_users_delete(request):
    pass

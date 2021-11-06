from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import User
from my_admin.forms import UserAdminRegistrationForm, UserAdminProfileForm


@user_passes_test(lambda user: user.is_staff)
def index(request):
    context = {'title': 'GeekShop - Панель Администратора'}
    return render(request, 'my_admin/index.html', context)


class UserListView(ListView):
    model = User
    template_name = 'my_admin/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('my_admin:admin_users')
    template_name = 'my_admin/admin-users-create.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('my_admin:admin_users')
    template_name = 'my_admin/admin-users-update-delete.html'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Редактирование пользовтаеля'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'my_admin/admin-users-update-delete.html'
    success_url = reverse_lazy('my_admin:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.safe_delete()
        return HttpResponseRedirect(success_url)

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda user: user.is_staff)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.safe_delete()
#     return HttpResponseRedirect(reverse('my_admin:admin_users'))

# @user_passes_test(lambda user: user.is_staff)
# def admin_users(request):
#     context = {'title': 'GeekShop - Пользователи', 'users': User.objects.all()}
#     return render(request, 'my_admin/admin-users-read.html', context)


# @user_passes_test(lambda user: user.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('my_admin:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'title': 'Админ-панель - Создание пользователя', 'form': form}
#     return render(request, 'my_admin/admin-users-create.html', context)


# @user_passes_test(lambda user: user.is_staff)
# def admin_users_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('my_admin:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {'title': 'Админ-панель - Обновление пользовтаеля', 'form': form, 'selected_user': selected_user}
#     return render(request, 'my_admin/admin-users-update-delete.html', context)

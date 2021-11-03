from django.urls import path

from my_admin.views import index, admin_users, admin_users_update, admin_users_delete, admin_users_create

app_name = 'my_admin'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users_create/', admin_users_create, name='admin_users_create'),
    path('users_update/', admin_users_update, name='admin_users_update'),
    path('users_delete/', admin_users_delete, name='admin_users_delete'),
]

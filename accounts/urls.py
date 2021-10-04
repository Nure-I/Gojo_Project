from django.urls import path

from . import views
from .views import PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('update', views.profile, name='update_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), name='change_password')
    path('password/', PasswordsChangeView.as_view(template_name='password_reset/password_change.html'), name='password'),
    path('password_success', views.password_success, name='password_success'),
]

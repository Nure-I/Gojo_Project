from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.success(request, "You're not Authorized to this page ")
                return redirect('dashboard')

        return wrapper_func

    return decorator


def customer_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            if group == 'realtors':
                return redirect('realtor')
            if group == 'customers':
                return view_func(request, *args, **kwargs)


    return wrapper_function

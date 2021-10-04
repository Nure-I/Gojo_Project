from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from contacts.models import Contact
from accounts.decorators import unauthenticated_user
from listings.models import Listing
from realtors.models import Realtor
from django.contrib.auth.models import Group
from .forms import UpdateProfile
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from array import *


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    group = Group.objects.get(name='customers')
                    user.groups.add(group)
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def profile(request):
    u_form = UpdateProfile()
    user = request.user
    update_user = User.objects.filter(username=user.username)
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            if username and email is not None:
                user.username = username
                user.email = email
                user.save()
                messages.success(request, 'Your profile Updated')
                return redirect('dashboard')
            else:
                return redirect('update_profile')
    else:
        messages.error(request, 'Your not Authenticated')
    context = {
        'u_form': u_form,
        'user': user
    }
    return render(request, 'accounts/edit_profile.html', context)


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    posted = Listing.objects.order_by('id').filter(owner=request.user)
    if request.user.groups.filter(name='realtors').exists():
        realtor = Realtor.objects.get(email__exact=request.user.email)
        is_realtor = request.user.groups.filter(name='realtors').exists()
        listings = Listing.objects.order_by('-list_date').filter(realtor=realtor)

        realtor_contacts = Contact.objects.order_by('-contact_date').filter(
            listing__in=listings.values_list('title', flat=True))
        print(realtor_contacts)
    else:
        is_realtor = False
        listings = None
        realtor_contacts = None
    context = {
        'contacts': user_contacts,
        'posted': posted,
        'listings': listings,
        'is_realtor': is_realtor,
        'realtors': realtor_contacts
    }
    return render(request, 'accounts/dashboard.html', context)


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    context = {

    }
    return render(request, 'password_reset/password_change_done.html', context)
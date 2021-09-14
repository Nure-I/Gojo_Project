from django.shortcuts import render, redirect
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices, listed_for, property_choices
from accounts.decorators import customer_only


# @customer_only
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    check = request.user.groups.filter(name='realtors').exists()
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listed_for': listed_for,
        'property_choices': property_choices,
        'check': check
    }
    if request.user.groups.filter(name='realtors').exists():
        return redirect('realtor')
    else:
        return render(request, 'pages/index.html', context)


def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('hire_date')

    # get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)

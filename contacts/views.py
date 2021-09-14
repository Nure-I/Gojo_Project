from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from listings.models import Listing
from django.shortcuts import get_object_or_404


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id)

        contact.save()

        # Send email
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info ',
            'nuredinibrahim40@gmail.com',
            [realtor_email, 'ibrahimsaladin1@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/' + listing_id)


def delete(request):
    # if request.user.groups.filter(name='realtors').exists():
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        print(listing_id)
        listing = request.POST.get('listing')
        print(listing)
        list = Listing.objects.get(title=listing)
        list.is_published = False
        list.save()

    return redirect('dashboard')


def post(request):
    # if request.user.groups.filter(name='realtors').exists():
    if request.method == 'POST':
        # listing_id = request.POST.get('listing_id')
        # print(listing_id)
        listing = request.POST.get('listing')
        print(listing)
        list = Listing.objects.get(title=listing)
        list.is_published = True
        list.save()

    return redirect('dashboard')


def cancel(request, contact_id):
    contacts = get_object_or_404(Contact, pk=contact_id)
    print(contact_id)
    # if request.method == 'POST':
    #     # listing_id = request.POST.get('listing_id')
    #     # print(listing_id)
    #     listing = request.POST.get('listing')
    #     print(listing)
    #     list = Listing.objects.get(title=listing)
    #     list.is_published = True
    #     list.save()

    return redirect('dashboard')

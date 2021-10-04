from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact, Feedback, Contactus, Payment
from listings.models import Listing
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


def contact(request):
    #  Check if user has made inquiry already
    if request.user.is_authenticated:
        if request.method == 'POST':
            listing_id = request.POST['listing_id']
            listing = request.POST['listing']
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            user_id = request.POST['user_id']
            realtor_email = request.POST['realtor_email']
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)
            else:
                contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                                  message=message,
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
    messages.error(request, 'Please login to made an inquiry ')
    return redirect('login')


# def delete(request):
#     # if request.user.groups.filter(name='realtors').exists():
#     if request.method == 'POST':
#         listing_id = request.POST.get('listing_id')
#         print(listing_id)
#         listing = request.POST.get('listing')
#         print(listing)
#         list = Listing.objects.get(title=listing)
#         list.is_published = False
#         list.save()
#
#     return redirect('dashboard')
#
#
# def post(request, listed_id):
#     listing = Listing.objects.get(id=listed_id)
#     print(listing)
#     listing.is_published = True
#     listing.save()
#
#     return redirect('dashboard')
def feedback(request):
    if request.method == 'POST':
        feedback = Feedback()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        feedback.name = name
        feedback.email = email
        feedback.subject = subject
        feedback.save()
        messages.success(request, 'Your feedback has been submitted, Thanks for your feedback ')
        return redirect('/')
    return render(request, 'pages/feedback.html')


def contactus(request):
    if request.method == 'POST':
        contact = Contactus()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, 'We will contact you soon, Thanks ')
        return redirect('contactus')
    return render(request, 'pages/contactus.html')


def cancel(request, contact_id):
    contacts = Contact.objects.get(id=contact_id)
    print(contacts)

    contacts.requested = 'Request canceled'
    contacts.save()

    return redirect('dashboard')


# check this one
def requests(request, request_id):
    contacted = Contact.objects.get(id=request_id)
    print(contacted)
    contacted.requested = 'Requested'
    contacted.save()
    return redirect('dashboard')


def accept(request, accept_id):
    contacts = get_object_or_404(Contact, pk=accept_id)
    # print(contacts[0].requested)

    contacts.requested = 'Request Accepted'
    contacts.save()

    return redirect('dashboard')


def reject(request, reject_id):
    contacts = get_object_or_404(Contact, pk=reject_id)
    print(contacts.requested)

    contacts.requested = 'Request Rejected'
    contacts.save()

    return redirect('dashboard')


# Paypal check out
def checkout(request, checkout_id):
    contacts = get_object_or_404(Contact, pk=checkout_id)
    listid = contacts.listing_id
    listing = get_object_or_404(Listing, pk=listid)
    # print(listing.price)

    return redirect('dashboard')


# paypal payment Complete
def payment_complete(request):
    body = json.loads(request.body)
    print("BODY:", body)
    contact = Contact.objects.get(listing_id=body['listingID'])
    listing = Listing.objects.get(title=contact.listing)
    print(contact)
    print(contact.listing)
    payment = Payment()
    payment.customer = contact
    payment.house = contact.listing
    payment.amount = listing.price
    payment.payment = 'Payment Completed'
    payment.save()
    send_mail(
        'Property Listing Inquiry',
        'There has been an inquiry for ' + contact.listing + '. Sign into the admin panel for more info ',
        'nuredinibrahim40@gmail.com',
        [contact.email, 'ibrahimsaladin1@gmail.com'],
        fail_silently=False
    )

    messages.success(request, 'Payment successfully completed')
    return JsonResponse('payment Completed!', safe=False)


def success(request, success_id):
    if 'TotalAmount' in request.GET:
        TotalAmount = request.GET['TotalAmount']
    if 'BuyerId' in request.GET:
        BuyerId = request.GET['BuyerId']
    if 'MerchantOrderId' in request.GET:
        MerchantOrderId = request.GET['MerchantOrderId']
    if 'MerchantCode' in request.GET:
        MerchantCode = request.GET['MerchantCode']
    if 'MerchantId' in request.GET:
        MerchantId = request.GET['MerchantId']
    if 'TransactionCode' in request.GET:
        TransactionCode = request.GET['TransactionCode']
    if 'TransactionId' in request.GET:
        TransactionId = request.GET['TransactionId']
    if 'Status' in request.GET:
        Status = request.GET['Status']
    if 'Currency' in request.GET:
        Currency = request.GET['Currency']
    if 'Signature' in request.GET:
        Signature = request.GET['Signature']
        print(Status)
        print(TotalAmount)
    listing = get_object_or_404(Listing, pk=success_id)
    listing.is_published = False
    listing.save()
    contact = Contact.objects.get(listing_id=success_id)
    contact.paid = True
    contact.save()
    payment = Payment()
    payment.customer = contact
    payment.house = contact.listing
    payment.amount = TotalAmount
    payment.transactionid = TransactionId
    payment.payment = 'Payment Completed'
    payment.save()
    # send_mail(
    #     'House Payment successfully completed ',
    #     'Your payment is successfully completed. Total Amount: ' + TotalAmount + Currency + '  Tansaction ID: '+ TransactionId +'  Merchant Id' + MerchantId + '  Thank You For Using our Service!',
    #     'nuredinibrahim40@gmail.com',
    #     [contact.email, 'ibrahimsaladin1@gmail.com'],
    #     fail_silently=False
    # )

    messages.success(request, 'Payment successfully completed')
    return redirect('dashboard')


def cancel_pay(request):
    return redirect('')

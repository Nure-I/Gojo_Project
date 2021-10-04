from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import bedroom_choices, state_choices, property_choices, listed_for, price_term
from django.contrib import messages, auth
from accounts.decorators import allowed_user
from realtors.models import Realtor
from contacts.models import Contact
from .models import Listing
from .forms import ListForm
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)


    contact = None
    customer = False
    if request.user.groups.filter(name='customers').exists():
        customer = True
        if Contact.objects.filter(listing_id=listing_id) is not None:
            contacts = Contact.objects.filter(listing_id=listing_id, user_id=request.user.id)
            if contacts:
                contact = contacts[0]
        else:
            contact = None
    owner = False
    if request.user.is_authenticated:
        if listing.owner == request.user:
            owner = True
    if request.user.groups.filter(name='realtors').exists():
        is_realtor = request.user.groups.filter(name='realtors').exists()
        realtor = Realtor.objects.get(email__exact=request.user.email)
    else:
        is_realtor = False
        realtor = None
    Service_pay = (int(listing.price * 0.02))
    Total_pay = (int(listing.price * 0.02) + listing.price)
    yene_obj = {
        "process": "Express",
        "successUrl": "http://127.0.0.1:8000/en/contacts/success/" + str(listing_id),
        "ipnUrl": "http://127.0.0.1:8000/ipn",
        "cancelUrl": "http://127.0.0.1:8000/en/contacts/cancel",
        "merchantId": "SB1258",
        "merchantOrderId": "val10.0",
        "expiresAfter": 24,
        "itemId": 1,
        "itemName": listing.title,
        "unitPrice": listing.price,
        "quantity": 1,
        "discount": 0.0,
        "handlingFee": Service_pay,
        "deliveryFee": 0.0,
        "tax1": 0.0,
        "tax2": 0.0,
    }
    context = {
        'listing': listing,
        'contact': contact,
        'is_realtor': is_realtor,
        'realtor': realtor,
        'owner': owner,
        'customer': customer,
        'yenepay': yene_obj,
        'Service_pay': Service_pay,
        'Total_pay': Total_pay
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Property Type
    if 'property' in request.GET:
        property = request.GET['property']
        if property:
            queryset_list = queryset_list.filter(property__icontains=property)

    # Search For
    if 'listed_for' in request.GET:
        listed = request.GET['listed_for']
        if listed:
            queryset_list = queryset_list.filter(listed_for__iexact=listed)

    # KEYWORDS
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # CITY
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # STATE
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # BEDROOMS
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # PRICE
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'listed_for': listed_for,
        'listings': queryset_list,
        'property_choices': property_choices,
        'values': request.GET

    }

    return render(request, 'listings/search.html', context)


def addlist(request):
    user = request.user
    form = ListForm()
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'property_choices': property_choices,
        'price_term': price_term,
        'listed_for': listed_for,
        'form': form
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ListForm(request.POST, request.FILES)
            # if form.is_valid():
            #     form.save()
            #     return redirect('/')
            # Method One
            # Get form values
            title = request.POST['title']
            address = request.POST['address']
            city = request.POST['city']
            region = request.POST['region']
            zipcode = request.POST['zipcode']
            bedrooms = request.POST['bedrooms']
            bathrooms = request.POST['bathrooms']
            garage = request.POST['garage']
            sqft = request.POST['sqft']
            lotsize = request.POST['lotsize']
            properties = request.POST['propertytype']
            # try form for image to work and authenticate
            priced = request.POST['priced']
            price_type = request.POST['price_term']
            listed = request.POST['listed_for']
            description = request.POST['description']
            photo_main = request.FILES['photomain']
            photo_1 = request.POST['image1']
            photo_2 = request.POST['image2']
            photo_3 = request.POST['image3']
            photo_4 = request.POST['image4']
            photo_5 = request.POST['image5']
            photo_6 = request.POST['image6']

            if Listing.objects.filter(address=address).exists():
                messages.error(request, 'That address is taken')
                return redirect('addlisting')
            else:
                if Listing.objects.filter(title=title).exists():
                    messages.error(request, 'That title is being used')
                    return redirect('addlisting')
                else:
                    # Looks good
                    list = Listing(owner=request.user,
                                   title=title,
                                   address=address,
                                   city=city,
                                   state=region,
                                   zipcode=zipcode,
                                   bedrooms=bedrooms,
                                   bathrooms=bathrooms,
                                   garage=garage,
                                   sqft=sqft,
                                   lot_size=lotsize,
                                   property=properties,
                                   price=priced,
                                   price_term=price_type,
                                   listed_for=listed,
                                   description=description,
                                   photo_main=photo_main,
                                   photo_1=photo_1,
                                   photo_2=photo_2,
                                   photo_3=photo_3,
                                   photo_4=photo_4,
                                   photo_5=photo_5,
                                   photo_6=photo_6
                                   )

                    list.save()
                    messages.success(request, 'You are now Posted a House ')
                    return redirect('/')
    else:
        return redirect('login')
    return render(request, 'listings/addlisting.html', context)


@allowed_user(allowed_roles=['realtors'])
def realtor(request):
    user = request.user.email
    realtor = Realtor.objects.get(email__exact=user)
    listings = Listing.objects.order_by('-list_date').filter(realtor=realtor)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'list': listings
    }

    return render(request, 'realtor/realtor.html', context)


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
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        print(listing_id)
        listing = request.POST.get('listing')
        print(listing)
        list = Listing.objects.get(title=listing)
        list.is_published = True
        list.save()

    return redirect('dashboard')


def trans(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text

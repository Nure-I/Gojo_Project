from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import bedroom_choices, state_choices, property_choices, listed_for, price_term
from django.contrib import messages, auth
from accounts.decorators import allowed_user
from realtors.models import Realtor
from .models import Listing
from .forms import ListForm


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
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
    context = {
        'listing': listing,
        'is_realtor': is_realtor,
        'realtor': realtor,
        'owner': owner
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

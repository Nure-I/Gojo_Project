from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('addlisting', views.addlist, name='addlisting'),
    path('realtor', views.realtor, name='realtor'),
    path('delete', views.delete, name='delete'),
    path('post', views.post, name='post')
]

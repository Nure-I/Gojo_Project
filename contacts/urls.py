from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('delete', views.delete, name='delete'),
    path('post', views.post, name='post'),
    path('<int:listing_id>', views.cancel, name='cancel')
]
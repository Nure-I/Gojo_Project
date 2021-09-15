from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('delete', views.delete, name='delete'),
    path('post', views.post, name='post'),
    path('<int:request_id>', views.requests, name='requests'),
    path('requests/<int:contact_id>', views.cancel, name='cancel'),
    path('accept/<int:accept_id>', views.accept, name='accept'),
    path('reject/<int:reject_id>', views.reject, name='reject')
]
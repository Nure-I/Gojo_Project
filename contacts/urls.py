from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('feedback', views.feedback, name='feedback'),
    path('contactus', views.contactus, name='contactus'),
    path('<int:request_id>', views.requests, name='requests'),
    path('checkout/<int:checkout_id>', views.checkout, name='checkout'),
    path('complete/', views.payment_complete, name='complete'),
    path('success/<int:success_id>', views.success, name='success'),
    path('cancel_pay', views.cancel_pay, name='cancel_pay'),
    path('requests/<int:contact_id>', views.cancel, name='cancel'),
    path('accept/<int:accept_id>', views.accept, name='accept'),
    path('reject/<int:reject_id>', views.reject, name='reject'),
    path('download_invoice/<int:house_id>', views.download_invoice, name='download_invoice'),
    path('upload_invoice', views.image_convert, name='upload_invoice')
]
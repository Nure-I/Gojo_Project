from django.db import models
from datetime import datetime
from listings.models import Listing


class Contact(models.Model):
    status = (
        ('Requested', 'Requested'),
        ('Request Accepted', 'Request Accepted'),
        ('Request Denied', 'Request Denied'),
        ('Request canceled', 'Request canceled')
    )
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    requested = models.CharField(max_length=100, choices=status, default="Requested")
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Payment(models.Model):
    customer = models.ForeignKey(Contact, on_delete=models.DO_NOTHING, default=1)
    house = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100, blank=True, default="yenePay")
    transactionid = models.CharField(max_length=150, blank=True)
    amount = models.CharField(max_length=100, blank=True)
    payment_status = models.CharField(max_length=100, default="Not Payed")
    payment_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.house


class Payment_invoice(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='invoice')
    confirmation = models.BooleanField(default=False)
    payment_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.TextField()

    def __str__(self):
        return self.name


class Contactus(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

from django.db import models
from datetime import datetime

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

    def __str__(self):
        return self.name

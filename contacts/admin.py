from django.contrib import admin

from .models import Contact, Feedback, Contactus, Payment


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'requested', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')


class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'house', 'payment_status', 'amount', 'payment_date')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Contactus, ContactusAdmin)
admin.site.register(Payment, PaymentAdmin)

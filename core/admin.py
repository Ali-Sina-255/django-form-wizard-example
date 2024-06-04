from django.contrib import admin

from . models import Guest, Booking,Business
admin.site.register(Guest)
admin.site.register(Booking)
admin.site.register(Business)
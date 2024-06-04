from django.contrib import admin

from . models import Guest, Booking,Business, User
admin.site.register(User)
admin.site.register(Guest)
admin.site.register(Booking)
admin.site.register(Business)
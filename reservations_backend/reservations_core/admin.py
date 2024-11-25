from django.contrib import admin
from .models import Address, Customer, Facility, Reservation

admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Facility)
admin.site.register(Reservation)

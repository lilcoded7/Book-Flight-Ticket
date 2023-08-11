from django.contrib import admin
from ticket.models.booking import Booking
from ticket.models.flight import Flight
# Register your models here.


admin.site.register(Booking)
admin.site.register(Flight)
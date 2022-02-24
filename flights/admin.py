from django.contrib import admin

from .models import Airline, Flight

class FlightInLine(admin.StackedInline):
    model = Flight
    extra = 1

class AirlineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['airline_name', 'airline_code']})
    ]


class FlightAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Airline Information', {'fields': ['airline_name', 'flight_number']}),
        ('Origin/Destination', {'fields': ['origin', 'destination']}),
        ('Departure and Arrival Time', {'fields': ['departure', 'arrival'], 'classes': ['collapse']})
    ]


admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)

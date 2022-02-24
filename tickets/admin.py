from django.contrib import admin

from .models import Reservation, Ticket


class TicketInline(admin.StackedInline):
    model = Ticket
    extra = 2


class ReservationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['flight', 'num_people', 'total_cost']})
    ]
    inlines = [TicketInline]

class TicketAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tickets', {'fields': ['seat', 'cost', 'ticket_class']})
    ]


admin.site.register(Reservation, ReservationAdmin)
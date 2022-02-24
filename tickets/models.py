from django.db import models

from flights.models import Flight

# Create your models here.

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    num_people = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

class Ticket(models.Model):
    first_class = 'F'
    business_class = 'B'
    main_cabin = 'M'
    ticket_class_choices = [
        (first_class, 'First Class'),
        (business_class, 'Business CLass'),
        (main_cabin, 'Main Cabin'),
    ]
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
    seat = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_class = models.CharField(
        max_length=1,
        choices=ticket_class_choices,
        default=None

    )

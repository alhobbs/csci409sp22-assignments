from django.db import models

from airports.models import Airport

 # Create your models here.
class Airline(models.Model):
    airline_name = models.CharField(max_length=100)
    airline_code = models.CharField(max_length=2)

class Flight(models.Model):
    origin = models.ForeignKey(Airport, related_name="flight_origin", on_delete=models.PROTECT)
    airline_name = models.ForeignKey(Airline, max_length=100, on_delete=models.PROTECT)
    destination = models.ForeignKey(Airport, related_name="flight_destination", on_delete=models.PROTECT)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    aircraft_type = models.CharField(max_length=10)
    flight_number = models.IntegerField()



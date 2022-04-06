from django.http import HttpResponse
from django.shortcuts import render
from .models import Flight
from .forms import FlightForm

def index(request):
    form = FlightForm
    return render(request, 'flights/index.html', {'form': form});


def search(request):
    form = FlightForm(request.POST)
    if form.is_valid():
        flights = Flight.objects.get(id=form.cleaned_data['flight_number'])
        return render(request, 'flights/flight_search.html', {'flight': flights})


def flight_search(request, origin, destination):
    return HttpResponse('Showing flights from ' + origin + ' to ' + destination);
from django.http import HttpResponse
from django.shortcuts import render
from .models import Reservation
from .forms import TicketForm
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    form = TicketForm()
    return render(request, 'tickets/index.html', {'form': form})

@login_required()
def search(request):
    form = TicketForm(request.POST)
    if form.is_valid():
        reservation = Reservation.objects.get(id=form.cleaned_data['confirmation_number'])
        return render(request, 'tickets/ticket_search.html', {'reservation': reservation})

def ticket_search(request, confirmation_number):
    return HttpResponse('Showing tickets for confirmation number: ' + str(confirmation_number));

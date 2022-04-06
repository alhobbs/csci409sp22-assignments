from django import forms

class FlightForm(forms.Form):
    Origin = forms.CharField(label='Origin')
    Destination = forms.CharField(label='Destination')
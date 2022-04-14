# Load path from django.urls
from django.contrib import admin
from django.urls import include, path
# Load this application views.py file

import airports.views

# Define url patterns
urlpatterns = [
    path('', airports.views.index),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('airports/', include('airports.urls')),
    path('flights/', include('flights.urls')),
    path('routes/', include('routes.urls')),
    path('tickets/', include('tickets.urls')),
]

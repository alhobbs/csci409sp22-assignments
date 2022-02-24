from django.contrib import admin

from .models import Airport, Runway

class RunwayInline(admin.StackedInline):
    model = Runway  # specify which model to use
    extra = 2   # How many to start w/

class AirportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'airport_code', 'is_open']}),
        ('Airport Address', {'fields': ['address', 'city', 'state', 'zipcode'], 'classes': ['collapse']})
    ]
    inlines = [RunwayInline]   # Load the RunwayInLine Class


admin.site.register(Airport, AirportAdmin)

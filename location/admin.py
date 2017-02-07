from django.contrib import admin

# Register your models here.
from location.models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('lat', 'long', 'pcn', 'timestamp')
    list_filter = ('pcn', 'timestamp')

admin.site.register(Location, LocationAdmin)
from django.contrib import admin

# Register your models here.
from location.models import Location, Student


class LocationAdmin(admin.ModelAdmin):
    list_display = ('lat', 'long', 'pcn', 'timestamp')
    list_filter = ('pcn', 'timestamp')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'givenName', 'mail')
    search_fields = ['pcn', 'givenName']


admin.site.register(Location, LocationAdmin)
admin.site.register(Student, StudentAdmin)

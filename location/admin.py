from django.contrib import admin

# Register your models here.
from location.models import Location, Student


class LocationAdmin(admin.ModelAdmin):
    list_display = ('lat', 'long', 'student', 'timestamp')
    list_filter = ('student', 'timestamp')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'givenName', 'mail')
    search_fields = ['u', 'givenName']


admin.site.register(Location, LocationAdmin)
admin.site.register(Student, StudentAdmin)

from django.contrib import admin

# Register your models here.
from location.models import Location, Student, Grade


class LocationAdmin(admin.ModelAdmin):
    list_display = ('lat', 'long', 'student', 'timestamp')
    list_filter = ('student', 'timestamp')


class GradeAdmin(admin.ModelAdmin):
    list_display = ('date', 'item', 'itemCode', 'grade', 'passed', 'student')
    list_filter = ('student', 'item', 'itemCode', 'item')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'givenName', 'mail')
    search_fields = ['u', 'givenName']


admin.site.register(Location, LocationAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Grade, GradeAdmin)
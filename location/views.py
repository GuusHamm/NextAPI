from location.models import Location, Student
from rest_framework import viewsets

from location.serializers import LocationSerializer, StudentSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_fields = ('pcn', 'timestamp')


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_fields = ('id', 'displayName', 'mail', 'personalTitle')

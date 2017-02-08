from location.models import Location, Student
from rest_framework import viewsets

from location.serializers import LocationSerializer, StudentSerializer, LocationReadSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_fields = ('student', 'timestamp')

    def get_serializer_class(self):
        if self.request.method in ('GET',):
            return LocationReadSerializer
        return LocationSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_fields = ('id', 'displayName', 'mail', 'personalTitle')

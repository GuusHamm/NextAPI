from location.models import Location, Student, Grade
from rest_framework import viewsets

from location.serializers import LocationSerializer, StudentSerializer, LocationReadSerializer, GradeSerializer, \
    GradeReadSerializer


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


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_fields = ('student', 'grade', 'item', 'itemCode')

    def get_serializer_class(self):
        if self.request.method in ('GET',):
            return GradeReadSerializer
        return GradeSerializer

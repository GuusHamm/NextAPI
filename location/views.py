from location.models import Location
from rest_framework import viewsets

from location.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

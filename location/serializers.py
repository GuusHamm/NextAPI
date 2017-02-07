from rest_framework import serializers

from location.models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('lat', 'long', 'pcn', 'timestamp')

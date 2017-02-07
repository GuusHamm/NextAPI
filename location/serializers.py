from rest_framework import serializers

from location.models import Location, Student


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('lat', 'long', 'pcn', 'timestamp')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'url', 'givenName', 'surName', 'initials', 'displayName', 'mail', 'photo', 'department',
                  'title', 'personalTitle', 'employeeId')

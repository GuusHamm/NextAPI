from location.models import Location, Student

from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'url', 'givenName', 'surName', 'initials', 'displayName', 'mail', 'photo', 'department',
                  'title', 'personalTitle', 'employeeId')


# class LocationSerializer(serializers.HyperlinkedModelSerializer):
class LocationSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=False, read_only=True)

    class Meta:
        model = Location
        fields = ('lat', 'long', 'student', 'timestamp')

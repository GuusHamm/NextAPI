from location.models import Location, Student

from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'url', 'givenName', 'surName', 'initials', 'displayName', 'mail', 'photo', 'department',
                  'title', 'personalTitle', 'employeeId')


# class LocationSerializer(serializers.HyperlinkedModelSerializer):
class LocationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Location
        fields = ('lat', 'long', 'student', 'timestamp')

    # def create(self, validated_data):
    #     print(validated_data)
    #     student_id = validated_data.student.id
    #
    #     get_object_or_404(Student, id=)
    #     student = Student.objects.get(id=student_id)
    #     validated_data.student = student
    #
    #     location  = Location.objects.create(**validated_data)
    #     return location


class LocationReadSerializer(LocationSerializer):
    student = StudentSerializer(many=False)



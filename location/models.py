from django.db import models


class Location(models.Model):
    lat = models.DecimalField(max_digits=15, decimal_places=8)
    long = models.DecimalField(max_digits=15, decimal_places=8)
    student = models.ForeignKey(
        'Student',
        on_delete=models.PROTECT)
    timestamp = models.DateTimeField()


class Student(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    url = models.CharField(max_length=255)
    givenName = models.CharField(max_length=255)
    surName = models.CharField(max_length=255)
    initials = models.CharField(max_length=255)
    displayName = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    photo = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    personalTitle = models.CharField(max_length=255)
    employeeId = models.IntegerField()

    def __str__(self):
        return self.id

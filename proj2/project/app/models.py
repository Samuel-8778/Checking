from django.db import models

# Create your models here.


class Employee(models.Model):

    objects = None
    employee_id = models.IntegerField
    position = models.CharField(max_length=20)

    def __str__(self):
        return self.employee_id, self.position


class Person(models.Model):
    objects = None
    person_id = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.person_id


class Address(models.Model):
    objects = None
    role = models.CharField(max_length=30)
    experience = models.IntegerField
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.role, self.experience, self.employee_id













from rest_framework import serializers
from .models import Employee, Person, Address


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class TaskSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class TaskSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"



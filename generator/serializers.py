
# connect python object to API
from dataclasses import fields
from rest_framework import serializers
from .models import employee
from rest_framework.serializers import ModelSerializer


class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = employee
        fields = ['firstname','lastname','role','department','mailAdd','employedDT','employeeID']
    def create(self, validated_data):
        return employee.objects.create(**validated_data)

# update serializer
class UpdateEmployeeSerializer(serializers.Serializer):

    firstname = serializers.CharField( max_length=25)
    lastname = serializers.CharField( max_length=25)
    role = serializers.CharField( max_length=200)
    department = serializers.CharField( max_length=200)
    mailAdd = serializers.EmailField(max_length=254)
    employedDT = serializers.DateField()
    employeeID = serializers.CharField( max_length=14)
    

    def create(self, validated_data):
        """
        Create and return a new `employee` instance, given the validated data.
        """
        return employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firstname = self.context['firstname']
        instance.lastname = self.context['lastname']
        instance.role = self.context['role']
        instance.department = self.context['department']
        instance.mailAdd = self.context['mailAdd']
        instance.employedDT = self.context['employedDT']
        instance.employeeID = self.context['employeeID']
        
        instance.save()
        return instance

    class Meta:
        model = employee
        fields = '__all__'
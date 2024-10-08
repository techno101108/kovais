from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'username','password','mobile', 'email', 'role','sucess', 'location','first_name','last_name']

class TotalEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'username', 'email', 'role','mobile', 'location','first_name','last_name']

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserDetails
        fields='__all__'


class SaloonOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model =SaloonOrder
        fields= '__all__'
        created_at = serializers.SerializerMethodField()
    # def get_created_at(self, obj):
    #     # Format the created_at field
    #     return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")


class GymOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =GymOrder
        fields= '__all__'
        created_at = serializers.SerializerMethodField()

   
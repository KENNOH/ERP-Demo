from dataclasses import fields
from rest_framework import serializers
from .models import CustomerNames



class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerNames
        fields = ['name','email','gender','phone_number','occupation','balance','created_on']
        

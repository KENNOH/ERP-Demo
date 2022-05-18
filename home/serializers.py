from select import select
from rest_framework import serializers
from .models import CustomerNames



class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerNames
        fields = ['name','email','gender','phone_number','occupation','balance','created_on']
        


class CreateCustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    balance = serializers.CharField(required=True)

    class Meta:
        model  = CustomerNames
        fields = ['name','email','gender','phone_number','occupation','balance']
    
    def validate(self, data):
        phone = data.get('phone_number')
        if len(phone) < 10: 
            raise serializers.ValidationError("Phone numbers should be 10 characters or more")
        if len(phone) > 13: 
            raise serializers.ValidationError("Phone numbers should be 13 characters or less")
        return data

    def create(self, validated_data):
        return CustomerNames.objects.create(**validated_data)
    
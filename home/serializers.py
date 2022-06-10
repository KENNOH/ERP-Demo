from rest_framework import serializers
from .models import CustomerNames
from .utils import send_confirmation_email


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




class UpdateCustomerSerializer(serializers.ModelSerializer):

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

    def update(self, instance, validated_data):
        name = instance.name
        email = instance.email
        message = 'Hello, '+name+ ' Your details have been updated on the erp platform. If you did not initiate this request, contact our customer service.'
        subject = 'Customer Details Update'
        mail_data = {'email':email,'message':message,'subject':subject}
        mail  = send_confirmation_email(mail_data)
        return super().update(instance, validated_data)

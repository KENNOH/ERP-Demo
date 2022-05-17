from tkinter.ttk import Style
from rest_framework import serializers
from django.contrib.auth.models import User



class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username','password']
        

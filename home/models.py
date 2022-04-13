from enum import auto
from statistics import mode
from django.db import models

# Create your models here.

class CustomerNames(models.Model):
    CHOICES = (
        ('HEALTH WORKERS','HEALTH WORKERS'),
        ('ENGINEER','ENGINEER'),
        ('DEVELOPER','DEVELOPER'),
        ('MANUAL WORKER','MANUAL WORKER'),
        ('CIVIL SERVANTS','CIVIL SERVANTS'),
        ('SOLDIER','SOLDIER'),
        ('STUDENT','STUDENT'),
        ('MINOR','MINOR'),
    )
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=150,unique=True)
    gender = models.BooleanField()
    phone_number = models.CharField(max_length=15,unique=True)
    occupation  =  models.CharField(max_length=50,choices=CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=10,default=0.00,decimal_places=2)





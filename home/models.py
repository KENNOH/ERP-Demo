from enum import auto
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.

class CustomerNames(models.Model):
    OCCUPATION_CHOICES = (
        ('HEALTH WORKERS','HEALTH WORKERS'),
        ('ENGINEER','ENGINEER'),
        ('DEVELOPER','DEVELOPER'),
        ('MANUAL WORKER','MANUAL WORKER'),
        ('CIVIL SERVANTS','CIVIL SERVANTS'),
        ('SOLDIER','SOLDIER'),
        ('STUDENT','STUDENT'),
        ('MINOR','MINOR'),
    )
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O','Others'),
    )
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=150,unique=True)
    gender = models.CharField(max_length=15,choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15,unique=True)
    occupation  =  models.CharField(max_length=50,choices=OCCUPATION_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=10,default=0.00,decimal_places=2)

    class Meta:
        verbose_name = 'Customer Name'
        verbose_name_plural = 'Customer Names'

    def __str__(self):
        return self.name + ' --- ' + self.email




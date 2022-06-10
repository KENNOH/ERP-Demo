import django_tables2 as tables
from .models import CustomerNames


class CustomerTable(tables.Table):

    class Meta:
        model = CustomerNames
        fields = ['name','email','gender','phone_number','occupation',"balance",'created_on']

        

import imp
from django.contrib import admin
from .models import CustomerNames


# Register your models here.
admin.site.site_header = 'ERP'
admin.site.site_title  = 'Welcome to ERP DEMO'
admin.site.index_title = 'Admin portal'


class AdminCustomerNames(admin.ModelAdmin):
    list_display = ['id','name','email','gender','phone_number','occupation','balance']
    list_display_links = ['id']
    list_per_page = 5
    search_fields = ['name','email','phone_number','occupation']
    list_filter = ['gender','occupation']


    class Meta:
        model = CustomerNames


admin.site.register(CustomerNames,AdminCustomerNames)

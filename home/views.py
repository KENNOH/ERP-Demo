from django.shortcuts import render
from .models import CustomerNames
from .tables import CustomerTable
from django_tables2 import RequestConfig
from django.core.paginator import Paginator
# Create your views here.


"""This is the default root index for the application this should be accesed from the browser on the link '127.0.0.1:8000'"""
def index(request):
    calc = 45 + 20
    name = 'My name is tech'

    """Queryset fetching all the data for customernames"""
    customer_names_set = CustomerNames.objects.all().order_by('created_on')

    """DJango Tables module"""
    customer_table = CustomerTable(customer_names_set)
    RequestConfig(request,paginate={'per_page':3}).configure(customer_table)

    """This is a custom table pagination module"""
    paginator = Paginator(customer_names_set,3)
    page_number = request.GET.get('page')
    paginator_module = paginator.get_page(page_number)


    """Dictionary containing all the variables we want to pass and show on the html"""    
    args = {'name':name,'calc':calc,'customer_names_queryset':customer_names_set,'customer_table':customer_table,
    'paginator_module':paginator_module}
    return render(request,'home/index.html',args)



from django.shortcuts import redirect, render
from .models import CustomerNames
from .tables import CustomerTable
from django_tables2 import RequestConfig
from django.core.paginator import Paginator
from .forms import AddCustomerForm, UpdateCustomerForm
from django.template.context_processors import csrf
from django.contrib import messages
# Create your views here.


"""This is the default root index for the application this should be accesed from the browser on the link '127.0.0.1:8000'"""
def index(request):
    calc = 45 + 20
    name = 'My name is tech'

    """Queryset fetching all the data for customernames"""
    customer_names_set = CustomerNames.objects.all().order_by('-created_on')

    """DJango Tables module"""
    customer_table = CustomerTable(customer_names_set)
    RequestConfig(request,paginate={'per_page':3}).configure(customer_table)

    """This is a custom table pagination module"""
    paginator = Paginator(customer_names_set,10)
    page_number = request.GET.get('page')
    paginator_module = paginator.get_page(page_number)


    """Dictionary containing all the variables we want to pass and show on the html"""    
    args = {'name':name,'calc':calc,'customer_names_queryset':customer_names_set,'customer_table':customer_table,
    'paginator_module':paginator_module}
    return render(request,'home/index.html',args)


def add_customers(request):
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.save()
            messages.add_message(request, messages.SUCCESS, 'Your data has been collected and submitted successfully.')
            return redirect('index')
        else:
            args = {'form':form}
            return render(request,'home/add-customer.html',args)
    else:
        form = AddCustomerForm()
        args = {'form':form}
        args.update(csrf(request))
        return render(request,'home/add-customer.html',args)



def update_customer(request,id):
    instance  = CustomerNames.objects.get(id=id)
    if request.method == 'POST':
        form  = UpdateCustomerForm(request.POST,instance=instance)
        if form.is_valid():
            form_instance = form.save(commit=False)
            name = form.cleaned_data['name']
            form.instance.name = name.upper()
            form_instance.save()
            messages.add_message(request, messages.SUCCESS, 'Your data has been updated successfully.')
            return redirect('index')
        else:
            args = {'form':form}
            return render(request, 'home/update-customer.html',args)
    else:
        form  = UpdateCustomerForm(instance=instance)
        args = {'form':form}
        args.update(csrf(request))
        return render(request,'home/update-customer.html',args)



def delete_customer(request,id):
    instance = CustomerNames.objects.get(id=id)
    instance.delete()
    messages.add_message(request, messages.INFO,'Customer has been deleted successfully.')
    return redirect('index')


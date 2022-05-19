from ast import keyword
from django.shortcuts import redirect, render
from .models import CustomerNames
from .tables import CustomerTable
from django_tables2 import RequestConfig
from django.core.paginator import Paginator
from .forms import AddCustomerForm, UpdateCustomerForm
from django.template.context_processors import csrf
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .utils import send_confirmation_email
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status, generics, filters
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
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


@login_required(login_url='/sign-in/')
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


@login_required(login_url='/sign-in/')
def update_customer(request,id):
    instance  = CustomerNames.objects.get(id=id)
    if request.method == 'POST':
        form  = UpdateCustomerForm(request.POST,instance=instance)
        if form.is_valid():
            form_instance = form.save(commit=False)
            name = form.cleaned_data['name']
            form_instance.name = name.upper()
            form_instance.save()
            messages.add_message(request, messages.SUCCESS, 'Your data has been updated successfully.')
            email = form.cleaned_data['email']
            message = 'Hello, '+name+ ' Your details have been updated on the erp platform. If you did not initiate this request, contact our customer service.'
            subject = 'Customer Details Update'
            mail_data = {'email':email,'message':message,'subject':subject}
            mail  = send_confirmation_email(mail_data)
            messages.add_message(request, messages.INFO, mail)
            return redirect('index')
        else:
            args = {'form':form}
            return render(request, 'home/update-customer.html',args)
    else:
        form  = UpdateCustomerForm(instance=instance)
        args = {'form':form}
        args.update(csrf(request))
        return render(request,'home/update-customer.html',args)



@login_required(login_url='/sign-in/')
def delete_customer(request,id):
    instance = CustomerNames.objects.get(id=id)
    email = instance.email
    name = instance.name
    message = 'Hello '+name+' Your details have been deleted on the erp platform. If you did not initiate this request, please contact the customer service.'
    subject = 'Customer Details Deletion!'
    mail_data = {'email':email,'message':message,'subject':subject}
    mail  = send_confirmation_email(mail_data)
    messages.add_message(request, messages.INFO, mail)
    instance.delete()
    messages.add_message(request, messages.INFO,'Customer has been deleted successfully.')
    return redirect('index')




def search_customers(request):
    search_keyword = request.GET['customer_search']
    if search_keyword != '':
        searched_queryset = CustomerNames.objects.all().filter(
        Q(name__icontains=search_keyword) | Q(email__icontains=search_keyword) | Q(gender__iexact=search_keyword) |
        Q(phone_number__icontains=search_keyword) | Q(occupation__icontains=search_keyword)| Q(balance__icontains=search_keyword)
        ).order_by('-created_on')

        """Date search"""
        # converted_keyword = datetime.strptime(search_keyword, '%m %d %Y')
        # searched_queryset = CustomerNames.objects.all().filter(created_on__gte=converted_keyword)

        """Search by greater than or equal to the value provide in search"""
        # searched_queryset = CustomerNames.objects.all().filter(balance__gte=search_keyword)
        
        """Search by greater than strictly to the value provide in search"""
        # searched_queryset = CustomerNames.objects.all().filter(balance__gt=search_keyword)

        """Search by less than or equal to to the value provide in search"""
        # searched_queryset = CustomerNames.objects.all().filter(balance__lte=search_keyword)

        """Search by less than strictly to the value provide in search"""
        # searched_queryset = CustomerNames.objects.all().filter(balance__lt=search_keyword)

        """This is a custom table pagination module"""
        paginator = Paginator(searched_queryset,10)
        page_number = request.GET.get('page')
        paginator_module = paginator.get_page(page_number)
        args = {'paginator_module':paginator_module,'search_keyword':search_keyword}

        return render(request,'home/index.html',args)
    else:
        return redirect('index')



class CustomersView(generics.ListAPIView,generics.CreateAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # user = request.user
        queryset = CustomerNames.objects.all()
        serializer = CustomerSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateCustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)



class CustomerUpdateView(generics.UpdateAPIView,generics.DestroyAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]



    def update(self, request,id):
        object_instance = CustomerNames.objects.get(id=id)
        serializer = UpdateCustomerSerializer(object_instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)


    def delete(self, request,id):
        object_instance = CustomerNames.objects.get(id=id)
        email = object_instance.email
        name = object_instance.name
        message = 'Hello '+name+' Your details have been deleted on the erp platform. If you did not initiate this request, please contact the customer service.'
        subject = 'Customer Details Deletion!'
        mail_data = {'email':email,'message':message,'subject':subject}
        mail  = send_confirmation_email(mail_data)
        object_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


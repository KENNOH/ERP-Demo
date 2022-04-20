from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^add-customers/',views.add_customers,name='add_customers'),
    url(r'^',views.index,name='index'),
]


"""This is the url config for the home application, this is where all the views are connected to the url"""
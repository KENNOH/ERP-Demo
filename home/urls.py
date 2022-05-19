from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^customers/',views.CustomersView.as_view(),name='get_create_customers'),
    url(r'^update-customers/(?P<id>[\w-]+)/$',views.CustomerUpdateView.as_view(),name='update_delete_customers'),
    url(r'^add-customers/',views.add_customers,name='add_customers'),
    url(r'^update-customer/(?P<id>[\w-]+)/$',views.update_customer,name='update_customer'),
    url(r'^delete-customer/(?P<id>[\w-]+)/$',views.delete_customer,name='delete_customer'),
    url(r'^search-customers/',views.search_customers,name='search_customers'),
    url(r'^',views.index,name='index'),
]


"""This is the url config for the home application, this is where all the views are connected to the url"""
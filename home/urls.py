from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^fetch-all-customers/',views.FetchCustomersView.as_view(),name='fetch_customers_endpoint'),
    url(r'^add-customers/',views.add_customers,name='add_customers'),
    url(r'^update-customer/(?P<id>[\w-]+)/$',views.update_customer,name='update_customer'),
    url(r'^delete-customer/(?P<id>[\w-]+)/$',views.delete_customer,name='delete_customer'),
    url(r'^search-customers/',views.search_customers,name='search_customers'),
    url(r'^',views.index,name='index'),
]


"""This is the url config for the home application, this is where all the views are connected to the url"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^',views.index,name='index'),
]


"""This is the url config for the home application, this is where all the views are connected to the url"""
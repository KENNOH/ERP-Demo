from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^sign-in/',views.sign_in,name='sign_in'),
    url(r'^register-user/',views.register_user,name='register_user'),
]


"""This is the url config for the authentication application, this is where all the views are connected to the urls.py file"""
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^password-reset/',auth_views.PasswordResetView.as_view(
        template_name='authentication/password_reset.html',
        email_template_name = 'authentication/password_reset_email',
        subject_template_name= 'authentication/password_reset_subject.txt',
        success_url = 'password_reset_confirmation'),name='password_reset'),
    url(r'^password-reset-confirm/(?P<uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z_\-]+)/$',auth_views.PasswordResetConfirmView.as_view(
        template_name = 'authentication/password_reset_confirm.html'
    ),name='password_reset_confirmation'),
    url(r'^sign-out/',views.sign_out,name='sign_out'),
    url(r'^sign-in/',views.sign_in,name='sign_in'),
    url(r'^register-user/',views.register_user,name='register_user'),
]


"""This is the url config for the authentication application, this is where all the views are connected to the urls.py file"""
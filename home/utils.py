import imp
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
import requests
import json



def send_confirmation_email(mail_data):
    try:
        subject = mail_data.get('subject')
        email_address = mail_data.get('email')
        message = mail_data.get('message')
        message_template = render_to_string('home/customer_email_template.html',{'message':message})
        email = EmailMessage(subject,message_template,from_email=settings.DEFAULT_FROM_EMAIL,to=[email_address])
        email.content_subtype = "html"
        email.send()
        return "Email sent to customer successfully"
    except:
        return "There was an error sending the email to customer"



def generate_jwt_token(request):
    """username and password vary, we have just hardcoded for easy learning but you can update yours or modify it to accept them as parameters"""
    username = ''
    password = ''

    auth_base_url = 'http://127.0.0.1:8000/'
    url  = '{}{}'.format(auth_base_url,'fetch-auth-token/')
    payload = {'username':username,'password':password}
    headers= {
    'Accept': 'application/json',                         
    'Content-Type': 'application/json; charset=utf-8'
    }
    response = requests.post(url,headers=headers,data=json.dumps(payload))
    if response.status_code == 200:
        data = response.json()['access']
        return data
    else:
        return messages.add_message(request, messages.ERROR, "An error occured fetching the token")
        
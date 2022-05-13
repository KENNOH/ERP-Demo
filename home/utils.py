import imp
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages



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
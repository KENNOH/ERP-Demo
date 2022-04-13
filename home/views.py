from django.shortcuts import render

# Create your views here.


"""This is the default root index for the application this should be accesed from the browser on the link '127.0.0.1:8000'"""
def index(request):
    calc = 45 + 20
    name = 'My name is tech'
    return render(request,'home/index.html',{'name':name,'calc':calc})

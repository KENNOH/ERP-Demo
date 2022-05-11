import imp
from statistics import mode
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q



class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'placeholder':'first name'}))
    last_name = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'placeholder':'last name'}))
    username = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'placeholder':'username'}))
    email = forms.EmailField(max_length=150,required=True,widget=forms.TextInput(attrs={'placeholder':'first_name'}))
    phone_number = forms.CharField(max_length=15,required=True,widget=forms.TextInput(attrs={'placeholder':'phone number'}))
    address = forms.CharField(max_length=150,required=False,widget=forms.TextInput(attrs={'placeholder':'address'}))


    class Meta:
        model = User
        fields =  (
            'first_name', 'last_name', 'username', 'email', 'phone_number', 'address'
        )


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter user name'}))
    password  = forms.CharField(max_length=150,required=True,widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))

    def clean(self,*args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user_object = User.objects.filter(Q(username__iexact=username))
        user = user_object.first()
        if user == None:
            raise forms.ValidationError("Incorrect user or password entered")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password or password entered")
        return super(UserLoginForm,self).clean(*args,**kwargs)
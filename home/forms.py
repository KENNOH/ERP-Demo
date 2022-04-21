from django import forms
from .models import CustomerNames



class AddCustomerForm(forms.ModelForm):
    name = forms.CharField(max_length=100,label='Enter Customer Name',widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Enter name here'}))


    class Meta:
        model = CustomerNames
        fields = ['name','email','gender','phone_number','occupation','balance']


    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if len(phone) < 10:
            raise forms.ValidationError("Phone numbers should be 10 characters or more in length")
        if len(phone) > 13:
            raise forms.ValidationError('Phone numbers should not exceed 13 characters in length')
        return phone




class UpdateCustomerForm(forms.ModelForm):

    class Meta:
        model = CustomerNames
        fields = ['name','email','gender','phone_number','occupation','balance']

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if len(phone) < 10:
            raise forms.ValidationError("Phone numbers should be 10 characters or more in length")
        if len(phone) > 13:
            raise forms.ValidationError('Phone numbers should not exceed 13 characters in length')
        return phone
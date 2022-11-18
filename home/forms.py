from socket import fromshare
from django import forms
from .models import Contacts

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contacts
        fields='__all__'
        labels={
            'cust_name':'Name',
            'cust_phone':'Phone',
            'cust_email':'Email',
            'cust_remark':'Remarks',
            
        }

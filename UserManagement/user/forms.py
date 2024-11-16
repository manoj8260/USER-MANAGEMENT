from django import forms
from user.models import *
import re
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','password']
        widgets = {'password': forms.PasswordInput}
        # help_texts = {'password': 'password must contain 1 number (0-9) ,password must contain 1 uppercase letters, password must contain 1 lowercase letters, password must contain 1 non-alpha numeric number, password is 8-16 characters with no space'}


    def clean_password(self):
        pw = self.cleaned_data.get('password')
        if re.match(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$', pw):
            return pw
        raise forms.ValidationError('invalid Password')  

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        exclude=['username']
        roles= [
        ('Owner', 'Owner'),
        ('Director', 'Director'),
        ('Finance Manager', 'Finance Manager'),
        ('General Manager', 'General Manager'),  
        ]
        widgets={'role':forms.Select(choices=roles)}
   


    def clean_mobile_no(self):
        mobile_no = self.cleaned_data.get('mobile_no')
        if re.match('^(\+91|\+91\-|0)? ?[789]\d{9}$', mobile_no):
            return mobile_no
        raise forms.ValidationError('Please enter a valid phone number like +91 1234567890')
    
    def clean_whatsapp_no(self):
        whatsapp_no = self.cleaned_data.get('whatsapp_no')
        if re.match('^(\+91|\+91\-|0)? ?[789]\d{9}$', whatsapp_no):
            return whatsapp_no
        raise forms.ValidationError('Please enter a valid phone number like +91 1234567890')

    





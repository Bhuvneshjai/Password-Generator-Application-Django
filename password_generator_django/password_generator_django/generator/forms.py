from django import forms

class UsernameForm(forms.Form):
    username = forms.CharField(max_length=100)

class PasswordForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    date_of_birth = forms.DateField(required=False)
    email_id = forms.EmailField(required=False)
    mobile_number = forms.CharField(max_length=15, required=False)
    
    include_name = forms.BooleanField(required=False)
    include_dob = forms.BooleanField(required=False)
    include_email = forms.BooleanField(required=False)
    include_mobile = forms.BooleanField(required=False)

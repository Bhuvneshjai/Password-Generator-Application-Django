from django.shortcuts import render, redirect
from django import forms
import random
import string

class UsernameForm(forms.Form):
    username = forms.CharField(max_length=100)

class PasswordForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.TextInput(attrs={'type': 'date'}))
    email_id = forms.EmailField(required=False)
    mobile_number = forms.CharField(max_length=15, required=False)

    include_name = forms.BooleanField(required=False)
    include_dob = forms.BooleanField(required=False)
    include_email = forms.BooleanField(required=False)
    include_mobile = forms.BooleanField(required=False)

def home(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            return redirect('password_generator', username=username)
    else:
        form = UsernameForm()
    return render(request, 'pages/home.html', {'form': form})

def password_generator(request, username):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            characters = ''
            if data['include_name']:
                characters += data['name']
            if data['include_dob']:
                characters += data['date_of_birth'].strftime('%Y%m%d')
            if data['include_email']:
                characters += data['email_id']
            if data['include_mobile']:
                characters += data['mobile_number']
            
            # Fallback to random characters if nothing is selected
            if not characters:
                characters = string.ascii_letters + string.digits + string.punctuation

            generated_password = ''.join(random.choice(characters) for _ in range(12))
            return render(request, 'pages/result_password.html', {'password': generated_password, 'username': username})
    else:
        form = PasswordForm()
    return render(request, 'pages/password_generator.html', {'form': form, 'username': username})

def logout(request):
    return redirect('home')

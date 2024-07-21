from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'pages/home.html')

def password(request):
    if request.method == 'POST':
        length = int(request.POST.get('length', 12))
        print(f"Length : {length}")
        
        uppercase = request.POST.get('uppercase') == 'on'
        print(f"Uppercase : {uppercase}")
        
        numbers = request.POST.get('numbers') == 'on'
        print(f"Numbers : {numbers}")
        
        symbols = request.POST.get('symbols') == 'on'
        print(f"Symbols : {symbols}")

        characters = string.ascii_lowercase
        print(f"Lowercase : {characters}")

        if uppercase:
            characters += string.ascii_uppercase
            print(f"Uppercase : {characters}")
        if numbers:
            characters += string.digits
            print(f"Numbers : {characters}")
        if symbols:
            characters += string.punctuation
            print(f"Symbols : {characters}")

        print(f"Random Choice : {random.choice(characters)}")

        generated_password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated Password : {generated_password}")

        return render(request, 'pages/password.html', {'password': generated_password})

    return render(request, 'pages/home.html')

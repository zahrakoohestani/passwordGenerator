from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters=list('asdfghjklqwertyuiopzxcvbnm')
    if request.GET.get('uppercase'):
        characters.extend(list('ASDFGHJKLQWERTYUIOPZXCVBNM'))
    if request.GET.get('symbols'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length=request.GET.get('length')
    length=int(length)
    thePassword=''
    for i in range(length):
        thePassword+=random.choice(characters)
    return render(request, 'generator/password.html', {'password':thePassword})

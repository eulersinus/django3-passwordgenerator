from django.shortcuts import render #allows to process html response
from django.http import HttpResponse #wandelt python code in http response um
import random

# Create your views here.

def home(request): #da wir bei urls darauf zugreifen, müssen wir sie auch deklarieren
    return render(request, 'generator/home.html') # seperate html which is returned



def password(request): # request referiert darauf, dass wir darauf zugreifen wollen

    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercases = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    special = list('!"§$%&/())=?`')

    length = int(request.GET.get('length', 12)) # 12 is the default length

    thepassword = ''

    if request.GET.get('uppercase'): # das ist natürlich 10 mal schlauer als das was ich gemacht habe
        characters.extend(uppercases)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('special'):
        characters.extend(special)

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password' : thepassword})

def about(request):
    return render(request, 'generator/about.html')
from distutils.command.build_scripts import first_line_re
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from requests import request
from contacts.models import Contact

# Create your views here.
def register(register):
    if request.method == 'POST':
        #get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email =  request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if password match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email exists in the database')
                    return redirect('register')
                else
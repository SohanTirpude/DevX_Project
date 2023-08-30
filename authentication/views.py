from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
import re
# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')


def singup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employee_id = request.POST.get('employee_id')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        employee_id_pattern = re.compile(r'^PSI-\d+$')
        valid_employee_id = employee_id_pattern.match(employee_id)

        email_id_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        valid_email = email_id_pattern.match(email_id)

        password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$!%^&*()_+{}:;<>,.?~[\]\\\-]).{8,}$')
        valid_password = password_pattern.match(password)

        if valid_employee_id and valid_email and valid_password:
            if password == confirm_password:
                my_user = User.objects.create_user(employee_id, email_id, password)
                my_user.firstname = first_name
                my_user.last_name = last_name

                my_user.save()
                messages.success(request, "Your acciunt has been created successfully.")


        my_user = User.objects.create_user(employee_id, email_id, password)
        my_user.firstname = first_name
        my_user.last_name = last_name

        my_user.save()
        messages.success(request, "Your acciunt has been created successfully.")

        return redirect('singin')

    return render(request, 'authentication/singup.html')

def singin(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')

        user = authenticate(employee_id = employee_id, email_id = email_id, password = password)
        if user is not None:
            login(request, user)
            return render(request, 'authentication/index.html')
        else:
            messages.error(request, 'Bad credential')
            return redirect('home')

    return render(request, 'authentication/singin.html')

def singout(request):
    return render(request, 'authentication/singout.html')
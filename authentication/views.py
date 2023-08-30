from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
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
            first_name = user.first_name
            return render(request, 'authentication/index.html',{'first_name':first_name})
        else:
            messages.error(request, 'Bad credential')
            return redirect('home')

    return render(request, 'authentication/singin.html')

def singout(request):
    return render(request, 'authentication/singout.html')
import json
from django import http
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required 
from .forms import *
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.models import Group
from .models import User, Section, Department, Tickets
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
# from django.db.models.expressions import Exists
# Create your views here.
@login_required
def index(request):
    user = User.objects.get(username= request.user)
    user_tickets = Tickets.objects.filter(employee=user).all()
    if request.user.is_authenticated:
        if user.groups.filter(name='Employees').exists():
            return render(request, 'eticket\profile_emp.html',{'user': user,'tickets': user_tickets})
        elif user.groups.filter(name='Maintenance').exists():
            return render(request, 'eticket\maintenance.html', {'user': user, 'tours': Tickets.objects.all()})
            
        # if user.groups.filter(name='Employees').exists():

    
    return render(request, 'eticket/login_master.html')
    
def login_master(request):
    # if post method!
    if request.method == "POST":
        loginform = LoginForm(request.POST or None)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            
            return render(request, 'eticket/login_master.html',{
                'form': LoginForm(),
                'message':'خطأ في اسم المستخدم او كلمة المرور'
            })
    # if get method!
    
    
    return render(request, 'eticket/login_master.html',{
        "loginform": LoginForm()
        })

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("login_master"))

def register_emp(request):
    # if method is post!
    if request.method == "POST":
        new_user = Register_empForm(request.POST or None)
        if new_user.is_valid():
            first_name = new_user.cleaned_data['first_name']
            last_name = new_user.cleaned_data['last_name']
            email = new_user.cleaned_data['email']
            username = new_user.cleaned_data['username']
            password = new_user.cleaned_data['password']
            confirm = new_user.cleaned_data['confirm']
            department = new_user.cleaned_data['department']
            section = new_user.cleaned_data['section']

            if password != confirm:
                return render(request, 'eticket/register_emp.html',{'error': 'الرمز السري غير مطابق', 'form': Register_empForm()})
            try:
                employee = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password, department=department, section=section)
                employee.groups.add(2)
                employee.save()
                return HttpResponseRedirect(reverse('index'))
            except IntegrityError:
                return render(request, 'eticket/register_emp.html',{'alert': 'تم ادخال اسم المستخدم مسبقا', 'form': Register_empForm()})

    return render(request, 'eticket/register_emp.html',{'form': Register_empForm()})

def register_maintenance(request):
    if request.method == "POST":
        new_user = Register_Maintenance(request.POST or None)
        if new_user.is_valid():
            first_name = new_user.cleaned_data['first_name']
            last_name = new_user.cleaned_data['last_name']
            email = new_user.cleaned_data['email']
            username = new_user.cleaned_data['username']
            password = new_user.cleaned_data['password']
            confirm = new_user.cleaned_data['confirm']
            
            if password != confirm:
                return render(request, 'eticket/register_maintenance.html',{'error': 'الرمز السري غير مطابق', 'form': Register_Maintenance()})
            try:
                employee = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                employee.section = Section.objects.get(section_name="الصيانة")
                employee.groups.add(1)
                employee.save()
                return HttpResponseRedirect(reverse('index'))
            except IntegrityError:
                return render(request, 'eticket/register_maintenance.html',{'alert': 'تم ادخال اسم المستخدم مسبقا', 'form': Register_Maintenance()})

    return render(request, 'eticket/register_maintenance.html',{'form': Register_Maintenance()})
@login_required()
def employee(request, user_id):
    user = User.objects.get(pk=user_id)
    user_tickets = Tickets.objects.filter(employee=user).all()

    return render(request, 'eticket/profile_emp.html',{
        'user': user,
        'tickets': user_tickets
    })

# def maintenance(request):
#     all_tickets = Tickets.objects.all()

@login_required()
def convert_ticket(request):
    employee = User.objects.get(username=request.user)
    if request.method == 'POST':
        memorandum = request.POST['memo']
        notes = request.POST['notes']
        print(memorandum)
        form = Ticket_Form(request.POST or None)
        print(form.errors)
        if form.is_valid():
            tour_type = form.cleaned_data['tour_type']
            tour_name = form.cleaned_data['tour_name']
            tour_date = form.cleaned_data['tour_date']
            tour_duration = form.cleaned_data['tour_duration']
            expected_end_tour = form.cleaned_data['expected_end_tour']
            # print(f"expected{expected_end_tour}")
            tour = Tickets(employee=employee, tour_type=tour_type, tour_name=tour_name, tour_date=tour_date, tour_duration=tour_duration, expected_end_tour=expected_end_tour)        
            print(tour)
        
            tour.save()
        # return HttpResponseRedirect(reverse('convert_ticket'))
        return HttpResponseRedirect(reverse('employee', args=(request.user.id,)))

    return render(request, 'eticket\convert_ticket.html',{
        'form': Ticket_Form()
    })

    


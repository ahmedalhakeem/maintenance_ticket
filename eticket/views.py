import json
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

def index(request):
    user = User.objects.get(username=request.user)
    if request.user.is_authenticated:
        if user.groups.filter(name='Employees').exists():
            return render(request, 'eticket\profile_emp.html',{'user': user})
        elif user.groups.filter(name='Maintenance').exists():
            return render(request, 'eticket\maintenance.html', {'user': user, 'tours': Tickets.objects.all()})
        else:
            return HttpResponse('dd')
        # if user.groups.filter(name='Employees').exists():


    return render(request, 'eticket/login_master.html',{
        'form': LoginForm()
    })
    
def login_master(request):
    # if post method!
    if request.method == "POST":
        loginform = LoginForm(request.POST or None)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']

            login_user = authenticate(request, username=username, password=password)
            login(request, login_user)
            return HttpResponseRedirect(reverse('index'))
    # if get method!
    else:
        loginform= LoginForm()
        return render(request, 'eticket/login_master.html',{
            "loginform": loginform
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
    

    return render(request, 'eticket/employee.html')

# def maintenance(request):
#     all_tickets = Tickets.objects.all()

@login_required()
def convert_ticket(request):
    employee = User.objects.get(username=request.user)
    form = Ticket_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            tour_type = form.cleaned_data['tour_type']
            tour_name = form.cleaned_data['tour_name']
            tour_date = form.cleaned_data['tour_date']

            tour = Tickets(employee=employee, tour_type=tour_type, tour_name=tour_name, tour_date=tour_date)
            tour.save()
            return HttpResponse('f')
    return render(request, 'eticket\convert_ticket.html',{
        'form': Ticket_Form()
    })

    

# Profile page for each employee 
# @login_required  
# def profile_emp(request, emp_id):
#     user = User.objects.get(pk=emp_id)
#     ticket = Tickets.objects.filter(employee=user).all()
#     ticket = ticket.order_by('-date')
    #print(ticket)
    #user_tickets = Problems.objects.filter(pk=user)
    # if user is not None:
    #     return render(request, "eticket/profile_emp.html",{
    #         "user": user,
    #         "ticket": ticket,
    #         "ticketform": ticketform            
    #     })
# profile page for manager
# @login_required
# def maintentenance_profile(request, user_id):
#     tickets = Tickets.objects.filter(ticket_status="accomplished")
#     user = User.objects.get(pk=user_id)
#     return render(request, "eticket/manager_profile.html",{
#         "user": user,
#         "all_tickets": tickets,
#         "ticket_form" : TicketForm()
#     })


# @csrf_exempt
# def tickets(request, emp_id):
#     if request.method != "POST":
#         return JsonResponse({"error": "POST method is required"})
    
#     data = json.loads(request.body)

#     user = User.objects.get(username=data['sender'])
#     print(user)
    #it_user = User.objects.get(username="")
    # title = data.get('title')
    # print(title)
    # description = data['description']
    # priority = data['priority']
    # reciever = User.objects.get(username="haiderk")

    # new_ticket = Tickets(title=title, ticket_priority=priority, description=description, employee=user, it_user=reciever)
    # new_ticket.save()
    #print(sender)

    # return JsonResponse({'success': "responded successfully"})

# @csrf_exempt
# def convert_ticket(request, user_id):
#     if request.method=='GET':
#         return HttpResponse("PuT method is required")
    #return JsonResponse({"error": "POST method is required"})

    # if request.method == 'PUT':

    #     data = json.loads(request.body)
    #     #query the converted ticket
    #     if data.get('id') is not None:
    #         ticket = Tickets.objects.get(pk=data['id'])
        
    #     it_user = User.objects.get(username = data.get('it_user'))
    #     ticket.it_user = it_user
    #     ticket.ticket_status = data.get('status')
    #     ticket.save()

    
    #it_user = User.objects.get(username=data['it_user'])
    #print(it_user)
        # print(ticket)

        # return JsonResponse({'success': "successfully converted"})
# submit function from IT user.
# @csrf_exempt        
# def submit_ticket(request, user_id):
#     if request.method == 'GET':
#         return JsonResponse({'Error': 'This function requires PUT method!'})
#     if request.method == 'PUT':
#         data = json.loads(request.body)
#         if data.get('id') is not None:
#             ticket = Tickets.objects.get(pk=data.get('id'))
        
#         ticket.ticket_status = data.get('status')
#         ticket.solution = data.get('solution')
#         ticket.save()
#         print(ticket)
#         return JsonResponse({'success': 'successfully submitted'})
import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required 
# from .forms import *
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.models import Group
from .models import User, Section, Department, Tickets
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
# Create your views here.
def index(request):

    return render(request, 'eticket/index.html')
    
def login_master(request):
    # if post method!
    if request.method == "POST":
        loginform = LoginForm(request.POST or None)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']
            
            
            login_user = authenticate(request, username=username, password=password)

            if login_user.groups.filter(name="manager").exists():

                login(request, login_user)
                return HttpResponseRedirect(reverse('manager_profile',args=(login_user.id,)))
                
    
            elif login_user.groups.filter(name="department_manager").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('dept_mgr_profile',args=(login_user.id,)))
                #return render(request, 'eticket/dep_mgr_profile.html')

            elif login_user.groups.filter(name="section manager").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('sec_mgr_profile',args=(login_user.id,)))
                #return render(request, "eticket/sec_mgr_profile.html")

            elif login_user.groups.filter(name="tech").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('it_profile',args=(login_user.id,)))
                #return render(request, "eticket/it_profile.html")

            elif login_user.groups.filter(name="employee").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('profile_emp',args=(login_user.id,)))
                #return render(request, "eticket/profile_emp.html")
            
            else: 
                return render(request, "eticket/error.html",{
                    "message": "You have no privilge access"
                })
    # if get method!
    else:
        loginform= LoginForm()
        return render(request, 'eticket/login_master.html',{
            "loginform": loginform
        })

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

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
            pc_code = new_user.cleaned_data['pc_code']
            department = new_user.cleaned_data['department']
            section = new_user.cleaned_data['section']

            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, 
            username=username, password=password,pc_code=pc_code, department=department, section=section)
            
            it_section = Section.objects.get(section_name="IT")
            print(it_section)
            if user.section != it_section:
                x=True
                user.groups.add(5)
            else:
                x=False
                user.groups.add(4)
            print(x)
            return HttpResponseRedirect(reverse('login_master'))
           

    else:
        new_user=Register_empForm()
        return render(request, 'eticket/register_emp.html',{
            "user": new_user
        })


# Profile page for each employee 
@login_required  
def profile_emp(request, emp_id):
    user = User.objects.get(pk=emp_id)
    ticket = Tickets.objects.filter(employee=user).all()
    ticket = ticket.order_by('-date')
    #print(ticket)
    ticketform = TicketForm()
    #user_tickets = Problems.objects.filter(pk=user)
    if user is not None:
        return render(request, "eticket/profile_emp.html",{
            "user": user,
            "ticket": ticket,
            "ticketform": ticketform            
        })
# profile page for manager
@login_required
def manager_profile(request, user_id):
    tickets = Tickets.objects.filter(ticket_status="accomplished")
    user = User.objects.get(pk=user_id)
    return render(request, "eticket/manager_profile.html",{
        "user": user,
        "all_tickets": tickets,
        "ticket_form" : TicketForm()
    })
# profile page for it team
@login_required
def it_profile(request, user_id):
    it_user = User.objects.get(pk=user_id)
    # Show all converted ticket to this user
    ticket = Tickets.objects.filter(it_user=it_user).order_by('-date')
    #ticket = TicketForm()
    return render (request, "eticket/it_profile.html",{
        "user": it_user,
        "ticket": ticket
        #"ticket" : ticket
    })
# profile page for department manager
@login_required
def dept_mgr_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    done_tickets = Tickets.objects.filter(ticket_status='accomplished')
    undone_tickets = Tickets.objects.filter(ticket_status='unaccomplished')
    return render(request, "eticket/dept_mgr_profile.html",{
        "user": user,
        "done_tickets": done_tickets,
        "undone_tickets" : undone_tickets
    })
# profile page for section manager
@login_required
def sec_mgr_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    tech_group = Group.objects.get(name="tech")
    it_users = User.objects.filter(groups=tech_group)
    
    tickets = Tickets.objects.all().order_by('-date')
    paginator = Paginator(tickets, 10)
    page_number = request.GET.get('page')
    tickets  = paginator.get_page(page_number)
    #tickets = tickets.order_by('-date').all()
    #for item in tickets:
    #    print(item.id)
    return render(request, 'eticket/sec_mgr_profile.html',{
        "user": user,
        "it_users": it_users,
        "tickets": tickets 
        #"ticket_form": TicketForm()
    })
@csrf_exempt
def tickets(request, emp_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST method is required"})
    
    data = json.loads(request.body)

    user = User.objects.get(username=data['sender'])
    print(user)
    #it_user = User.objects.get(username="")
    title = data.get('title')
    print(title)
    description = data['description']
    priority = data['priority']
    reciever = User.objects.get(username="haiderk")

    new_ticket = Tickets(title=title, ticket_priority=priority, description=description, employee=user, it_user=reciever)
    new_ticket.save()
    #print(sender)

    return JsonResponse({'success': "responded successfully"})

@csrf_exempt
def convert_ticket(request, user_id):
    if request.method=='GET':
        return HttpResponse("PuT method is required")
    #return JsonResponse({"error": "POST method is required"})

    if request.method == 'PUT':

        data = json.loads(request.body)
        #query the converted ticket
        if data.get('id') is not None:
            ticket = Tickets.objects.get(pk=data['id'])
        
        it_user = User.objects.get(username = data.get('it_user'))
        ticket.it_user = it_user
        ticket.ticket_status = data.get('status')
        ticket.save()

    
    #it_user = User.objects.get(username=data['it_user'])
    #print(it_user)
        print(ticket)

        return JsonResponse({'success': "successfully converted"})
# submit function from IT user.
@csrf_exempt        
def submit_ticket(request, user_id):
    if request.method == 'GET':
        return JsonResponse({'Error': 'This function requires PUT method!'})
    if request.method == 'PUT':
        data = json.loads(request.body)
        if data.get('id') is not None:
            ticket = Tickets.objects.get(pk=data.get('id'))
        
        ticket.ticket_status = data.get('status')
        ticket.solution = data.get('solution')
        ticket.save()
        print(ticket)
        return JsonResponse({'success': 'successfully submitted'})
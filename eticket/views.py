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
from .models import User, Section, Department, Tickets, Ticket_Reply, Allocation
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from datetime import datetime
import datetime
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import StringIO, BytesIO
# Create your views here.
@login_required
def index(request):
    # print(datetime.time)
    user = User.objects.get(username= request.user)
    user_tickets = Tickets.objects.filter(employee=user).all().order_by('-ticket_date')
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'eticket/index.html',{
                'cars': Cars.objects.all(),
                'drivers': Drivers.objects.all(),
                'section': Section.objects.all()
            })
        if user.groups.filter(name='Employees').exists():
            return render(request, 'eticket\profile_emp.html',{'user': user,'tickets': user_tickets})
        elif user.groups.filter(name='Maintenance').exists():
            return render(request, 'eticket\maintenance.html', {'user': user, 'tours': Tickets.objects.exclude(unallocated_days=0).order_by('-tour_date')})
            
        # if user.groups.filter(name='Employees').exists():

    
    return render(request, 'eticket/login_master.html')
@never_cache
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
                'loginform': LoginForm(request.POST or None),
                'message':'خطأ في اسم المستخدم او كلمة المرور'
            })
    # if get method!
    
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'eticket/login_master.html',{
            "loginform": LoginForm()
            })

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("login_master"))

@login_required
def register_emp(request):
    # if method is post!
    if request.method == "POST":
        new_user = Register_empForm(request.POST or None)
        print(new_user.errors)
        if new_user.is_valid():
            first_name = new_user.cleaned_data['first_name']
            last_name = new_user.cleaned_data['last_name']
            email = new_user.cleaned_data['email']
            username = new_user.cleaned_data['username']
            password = new_user.cleaned_data['password']
            confirm = new_user.cleaned_data['confirm']
            department = new_user.cleaned_data['department']
            # section = new_user.cleaned_data['section']
            role = new_user.cleaned_data['role']
            print(role)

            if password != confirm:
                return render(request, 'eticket/register_emp.html',{'error': 'الرمز السري غير مطابق', 'form': Register_empForm()})
            try:
                employee = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password, department=department, role=role)
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
            role = new_user.cleaned_data['role']
            password = new_user.cleaned_data['password']
            confirm = new_user.cleaned_data['confirm']
            
            if password != confirm:
                return render(request, 'eticket/register_maintenance.html',{'error': 'الرمز السري غير مطابق', 'form': Register_Maintenance()})
            try:
                employee = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, role=role, password=password)
                employee.section = Section.objects.get(section_name="الصيانة")
                employee.groups.add(1)
                employee.save()
                return HttpResponseRedirect(reverse('index'))
            except IntegrityError:
                return render(request, 'eticket/register_maintenance.html',{'alert': 'تم ادخال اسم المستخدم مسبقا', 'form': Register_Maintenance()})

    return render(request, 'eticket/register_maintenance.html',{'form': Register_Maintenance()})

def add_car(request):
    pass
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
            tour = Tickets(employee=employee, tour_type=tour_type, tour_name=tour_name, tour_date=tour_date, tour_duration=tour_duration, expected_end_tour=expected_end_tour, unallocated_days= tour_duration)        
            if len(memorandum):
                tour.memorandum= memorandum
            if len(notes):
                tour.notes= notes
        
            tour.save()
        
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'eticket\convert_ticket.html',{
        'form': Ticket_Form()
    })

def allocate_tour(request, tour_id):
    tour = Tickets.objects.get(pk=tour_id)
    print(tour.tour_name)
    if request.method =='POST':
        allocate_form = Ticket_Reply_Form(request.POST or None)
        if allocate_form.is_valid():
            driver = allocate_form.cleaned_data['driver']
            car = allocate_form.cleaned_data['car']
            memo_status = allocate_form.cleaned_data['memo_statue']
            notes = allocate_form.cleaned_data['notes']
            ticket_reply = Ticket_Reply(ticket= tour,driver_name=driver, car=car, notes=notes, memorandum_statue=memo_status)
            if ticket_reply is not None:
                ticket_reply.save()
        return HttpResponseRedirect(reverse('index'))      
    return render(request, 'eticket/allocate_tour.html',{
        'tour': tour,
        'reply_form': Ticket_Reply_Form()
    })

def get_allocations(request):
    drivers = list(Drivers.objects.all().values())
    cars = list(Cars.objects.all().values())
    return JsonResponse({'cars': cars, 'drivers':drivers}, safe=False)
 
def send_memo_status(request, id):
    ticket = Tickets.objects.get(pk=id)
    memo_state = request.GET.get('memo_state')
    memo_note = request.GET.get('memo_note')
    if Ticket_Reply.objects.filter(ticket=ticket).exists():
        reply= Ticket_Reply.objects.get(ticket=ticket)
        reply.memorandum_statue= memo_state
        reply.save()
        if memo_state == 'تم الاستلام':
            ticket.status= True
            ticket.save()
        return JsonResponse({'msg':'تم تحديث حالة المذكرة'})
    memo_ack = Ticket_Reply(ticket=ticket, notes=memo_note, memorandum_statue = memo_state)
    memo_ack.save()
    
    if memo_state == "لم يتم استلام المذكرة":
        return JsonResponse({'msg': 'حالة المذكرة معلقة'}, safe=False)
    elif memo_state == "خطأ في المذكرة":
        return JsonResponse({"msg": 'خطأ في المذكرة'}, safe=False)
    ticket.status = True
    ticket.save()  
    list_memo_state = list(Ticket_Reply.objects.filter(id= memo_ack.id).values())  
    return JsonResponse({'data': list_memo_state}, safe=False)

def allocate_per_day(request, id):
    ticket = Tickets.objects.get(pk=id)
    ticket_reply = Ticket_Reply.objects.get(ticket=ticket)
    date = request.GET.get('date')
    car = Cars.objects.get(car_type= request.GET.get('car'))
    driver = Drivers.objects.get(driver_name= request.GET.get('driver'))
    allocation = Allocation(reply= ticket_reply, driver_name= driver, car=car, allocate_date= date, state=True)
    ticket.unallocated_days= ticket.unallocated_days - 1
    ticket.save()
    allocation.save()
    return JsonResponse({'data': 'success'},safe=False)

def check_allocation_status(request, id):
    ticket= Tickets.objects.get(pk=id)
    ticket_reply = Ticket_Reply.objects.get(ticket=ticket)
    allocations = list(Allocation.objects.filter(reply=ticket_reply).values())

    return JsonResponse(allocations, safe=False)
def show_replied_ticket(request, id):
    ticket = Tickets.objects.get(pk=id)
    try:
        memo_replied = Ticket_Reply.objects.get(ticket=ticket)
        if Allocation.objects.filter(reply = memo_replied).exists():    
            allocation = Allocation.objects.filter(reply = memo_replied)    
        
            return render(request, 'eticket/ticket_profile.html',{
                "allocations": allocation,
                'memo_replied': memo_replied,
                'ticket' :ticket
            })
        else:
            return render(request, 'eticket/ticket_profile.html',{
                'memo_replied': memo_replied,
                'ticket' :ticket,
                'message': 'لم يتم تخصيص عجلة حتى الان.. يرجى الانتظار رجاءا'
            })
        
    except 	Ticket_Reply.DoesNotExist:
        return render(request, 'eticket/ticket_profile.html',{
            'ticket': ticket,
            "state": "لم  يتم تأكيد استلام المذكرة. يرجى انتظار تأكيدها"
        })
   
def show_pdf(request, id):
    ticket = Tickets.objects.get(id=id)
    if not Ticket_Reply.objects.filter(ticket=ticket).exists():
        return render(request, 'eticket/send_status.html')
    reply = Ticket_Reply.objects.get(ticket=ticket)
    allocations = Allocation.objects.filter(reply = reply)
    template_path = 'eticket/report.html'
    context = {'ticket': ticket, 'reply': reply, 'allocations': allocations}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), dest=response)
    print(pisa_status)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def specify_period(request):

    return render(request, 'eticket/specify_period.html')
def show_specified(request):
    type= request.GET.get('type')
    start = request.GET.get('start')
    end = request.GET.get('end')
    tickets = list(Tickets.objects.filter(tour_type= type).filter(tour_date__range=[start, end]).values())
    result = []
    new_ticket = {'tickets': tickets}
    # print(new_ticket)   
    
    for ticket in tickets:
        # print(ticket['id'])
        user = User.objects.get(id=ticket['employee_id'])
        ticket['employee_id']=user.first_name
        # result.append(ticket)
        if Ticket_Reply.objects.filter(ticket=ticket['id']).exists():
            ticket_reply = Ticket_Reply.objects.get(ticket=ticket['id'])
            if Allocation.objects.filter(reply=ticket_reply).exists():
                allocation =list(Allocation.objects.filter(reply=ticket_reply).values())
                # print(allocation[0]) 
                drivers = []
                for item in allocation:
                    driver = Drivers.objects.get(id=item['driver_name_id'])
                    item['driver_name_id']= driver.driver_name
                    drivers.append(item['driver_name_id'])
                ticket['drivers'] = drivers
                result.append(ticket)
                    # result.append(item['driver_name_id'])
                    # driver_name = item["driver_name_id"]
                # result.append(driver_name)
                
            else:
                print("B")
                    
            
    print(result)   
    return JsonResponse({'data':result}, safe=False) 
    # return JsonResponse({'data':tickets}, safe=False)
def get_sections(request):
    department = Department.objects.get(department_name='الاتصالات')
    department is not None
    sections=list(Section.objects.filter(sections=department).values())
    print(sections)
    return JsonResponse(sections, safe=False)
def get_all_non_dept_sections(request):
    department = Department.objects.get(department_name='الاتصالات')
    sections = list(Section.objects.all().exclude(sections=department).values())
    print(sections)
    return JsonResponse(sections, safe=False)


def done_tickets(request):
    tickets = Tickets.objects.filter(unallocated_days=0).all().order_by('-id')
    cars = Cars.objects.all()
    drivers = Drivers.objects.all()
    if tickets=="":
        return render(request, 'eticket/done_tickets.html',{
            'message': 'لا يوجد تذاكر منجزة حاليا'
        })
    else:
        return render(request, 'eticket/done_tickets.html',{
            'tickets': tickets,
            'cars': cars,
            'drivers': drivers
        })
#  View allocated ticket
def view_allocations(request, ticket_id):
    ticket = Tickets.objects.get(id= ticket_id)
    ticket_reply = Ticket_Reply.objects.get(ticket=ticket)
    allocations = list(Allocation.objects.filter(reply= ticket_reply).values())
    for allocation in allocations:
        driver = Drivers.objects.get(id = allocation['driver_name_id'])
        allocation['driver_name_id'] = driver.driver_name
        car = Cars.objects.get(id=allocation['car_id'])
        allocation['car_id'] = car.car_type
    return JsonResponse({'data': allocations}, safe=False)

def edit_allocated_saved(request, id):
    allocation = Allocation.objects.get(pk=id)
    car = Cars.objects.get(car_type= request.GET.get('car'))
    driver = Drivers.objects.get(driver_name=request.GET.get('driver'))
    allocation.driver_name = driver
    allocation.car = car
    allocation.allocate_date = request.GET.get('date')
    allocation.save()
    print(allocation)
    return JsonResponse({'data': 'success'}, safe=False)
    
def ticket_info(request, id):
    ticket = list(Tickets.objects.filter(pk = id).values())
    return JsonResponse(ticket[0], safe=False)

def saved_edited_ticket(request, id):
    ticket = Tickets.objects.get(pk=id)
    ticket.tour_name = request.GET.get('title')
    ticket.tour_title = request.GET.get('type')
    # ticket.tour_date = request.GET.get('st_date')
    date_string_format = request.GET.get('st_date')
    end_date_string_format = request.GET.get('end_date')
    end_date_strip = end_date_string_format.rstrip()
    st_date_strip = date_string_format.rstrip()
    ticket.tour_date = st_date_strip
    ticket.expected_end_tour = end_date_strip
    ticket.tour_duration = request.GET.get('days')
    # ticket.expected_end_tour = request.GET.get('end_date')
    ticket.notes = request.GET.get('team')
    ticket.save()
    print(ticket)
    return JsonResponse({'data': 'success'}, safe=False)


def add_car(request):
    car = request.GET.get('car')
    if Cars.objects.filter(car_type=car).exists():
        return JsonResponse({'message': 'هذه المركبة تم اضافتها مسبقا'})
    new_car= Cars(car_type=car)
    new_car.save()
    return JsonResponse({'message': 'تم اضافة مركبة جديدة الى القائمة'})

def add_driver(request):
    driver = request.GET.get('driver')
    if Drivers.objects.filter(driver_name=driver).exists():
        return JsonResponse({'message': 'هذا الاسم تم اضافته مسبقا'})
    new_driver = Drivers(driver_name=driver)
    new_driver.save()
    return JsonResponse({'message': 'تم اضافة سائق جديد'})


from django import forms
from django.forms import fields, widgets
from eticket.models import *
from django.conf import settings

class LoginForm(forms.Form):
    username = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class':'un', 'placeholder': 'Username', 'align': 'center',}))
    password = forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'class': 'pass', 'placeholder': 'Password', 'align':'center',}))


class Register_empForm(forms.Form):
    first_name = forms.CharField(label="الاسم الاول", required=True, widget=forms.TextInput(attrs={'class':'inputform', 'placeholder':'ادخل الاسم الاول',}))
    last_name = forms.CharField(label="الاسم الاخير", required=True, widget=forms.TextInput(attrs={'class': 'inputform', 'placeholder': "ادخل الاسم الاخير", }))
    department = forms.ModelChoiceField(label="القسم", required=False,initial="choose_department", queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'inputform', 'placeholder':'','id': 'department'})) 
    # section = forms.ModelChoiceField(label="الشعبة", required=True,  queryset=Section.objects.all(), widget=forms.Select(attrs={'class': 'inputform', 'placeholder':'', 'id':'section'}))
    role = forms.CharField(label="الموقع الوظيفي", required=False, widget=forms.TextInput(attrs={'class': 'inputform','placeholder': 'ادخل الموقع الوظيفي',})) 
    email = forms.EmailField(label="البريد الالكتروني", required=True, widget=forms.EmailInput(attrs={'class': 'inputform', 'placeholder': 'ادخل البريد الالكتروني', }))
    username = forms.CharField(label="اسم المستخدم", required=True, widget=forms.TextInput(attrs={'class':'inputform', 'placeholder': 'ادخل اسم المستخدم',}))
    password = forms.CharField(label="كلمة السر", required=True, widget=forms.PasswordInput(attrs={'class':'inputform', 'placeholder': 'ادخل كلمة السر', }))
    confirm = forms.CharField(label="اعادة كلمة السر", required=True, widget=forms.PasswordInput(attrs={'class':'inputform', 'placeholder': 'اعد كتابة كلمة السر', }))
    
    
class Register_Maintenance(forms.Form):
    first_name = forms.CharField(label="الاسم الاول", required=True, widget=forms.TextInput(attrs={'class':'inputform', 'placeholder':'Enter your first name',}))
    last_name = forms.CharField(label="الاسم الاخير", required=True, widget=forms.TextInput(attrs={'class': 'inputform', 'placeholder': "Enter your last name", }))
    email = forms.EmailField(label="البريد الالكتروني", required=True, widget=forms.EmailInput(attrs={'class': 'inputform', 'placeholder': 'enter your email id', }))
    username = forms.CharField(label="اسم المستخدم", required=True, widget=forms.TextInput(attrs={'class':'inputform', 'placeholder': 'Enter your username',}))
    role = forms.CharField(label="الموقع الوظيفي", required=False, widget=forms.TextInput(attrs={'class': 'inputform','placeholder': 'ادخل الموقع الوظيفي',})) 
    password = forms.CharField(label="الرمز السري", required=True, widget=forms.PasswordInput(attrs={'class':'inputform', 'placeholder': 'Enter your password', }))
    confirm = forms.CharField(label="اعادة كتابة الرمز", required=True, widget=forms.PasswordInput(attrs={'class':'inputform', 'placeholder': 'Enter your password', }))
    

class Ticket_Form(forms.Form):
    tour_type = forms.ChoiceField(required=True,label='نوع الجولة', widget=forms.Select(attrs={'class':'inputform style-uniform', 'id':"",}), choices=[('داخلية', 'داخلية'),('خارجية','خارجية')])
    tour_name = forms.CharField( required=True,label='عنوان الجولة', widget=forms.TextInput(attrs={'class': 'inputform style-uniform'}))
    tour_date = forms.DateField(required=True,label='تاريخ بدايةالجولة', widget=widgets.DateInput(attrs={'class': 'inputform style-uniform','type':'date', 'id':"start"}))
    tour_duration = forms.IntegerField(required=True,label='عدد ايام الجولة', widget=widgets.NumberInput(attrs={'class':'inputform style-uniform', 'id':'tour-days', "lang":"ar_SA" }))  
    # expected_end_tour = forms.CharField(required=False,disabled=True,label='تاريخ نهاية الجولة المتوقع', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'end'}))
    expected_end_tour = forms.DateField(required=False,label='تاريخ نهاية الجولة المتوقع', widget=widgets.DateInput(attrs={'type': 'date','class': 'inputform style-uniform', 'id': 'end'}))
    
class Send_memo_confirm(forms.Form):
    memo_statue= forms.ChoiceField(required=True, label='حالة المذكرة', widget=forms.Select(attrs={'class': 'memo-select form-control'}),choices=[('تم الاستلام', "تم الاستلام"), ('لم يتم استلام المذكرة', 'لم يتم استلام المذكرة'), ('خطأ في المذكرة', 'خطأ في المذكرة')])
    notes = forms.CharField(required=False, label='ملاحطات', widget=forms.Textarea(attrs={'id': 'memos','class': 'memo-note form-control', 'placeholder': 'اكتب ملاحظات اخرى ان وجدت!'}))

class Ticket_Reply_Form(forms.Form):
    driver = forms.ModelChoiceField(required=True,  queryset=Drivers.objects.all(), label="اسم السائق", widget=forms.Select(attrs={'class':'form-control'}))
    car = forms.ModelChoiceField(required=True, label="اسم المركبة", widget=forms.Select(attrs={'class':'form-control'}), queryset=Cars.objects.all())

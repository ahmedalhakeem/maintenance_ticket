from django import forms
from django.forms import fields, widgets
from eticket.models import *

class LoginForm(forms.Form):
    username = forms.CharField(label="اسم المستخدم",  required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username',}))
    password = forms.CharField(label="كلمة المرور", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))


class Register_empForm(forms.Form):
    first_name = forms.CharField(label="الاسم الاول", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name',}))
    last_name = forms.CharField(label="الاسم الاخير", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your last name", }))
    department = forms.ModelChoiceField(label="القسم", required=False, queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Select Department',})) 
    section = forms.ModelChoiceField(label="الشعبة", required=True, queryset=Section.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Select Section',})) 
    email = forms.EmailField(label="البريد الالكتروني", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter your email id', }))
    username = forms.CharField(label="اسم المستخدم", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your username',}))
    password = forms.CharField(label="الرمز السري", required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your password', }))
    confirm = forms.CharField(label="اعادة كتابة الرمز", required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your password', }))
    
    # pc_code = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'PC-code', }))
class Register_Maintenance(forms.Form):
    first_name = forms.CharField(label="الاسم الاول", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name',}))
    last_name = forms.CharField(label="الاسم الاخير", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your last name", }))
    email = forms.EmailField(label="البريد الالكتروني", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter your email id', }))
    username = forms.CharField(label="اسم المستخدم", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your username',}))
    password = forms.CharField(label="الرمز السري", required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your password', }))
    confirm = forms.CharField(label="اعادة كتابة الرمز", required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your password', }))
    

class Ticket_Form(forms.Form):
    tour_type = forms.ChoiceField(required=True,label='نوع الجولة', widget=forms.Select(attrs={'class':'form-control'}), choices=[('داخلية', 'داخلية'),('خارجية','خارجية')])
    tour_name = forms.CharField( required=True,label='عنوان الجولة', widget=forms.TextInput(attrs={'class': 'form-control'}))
    tour_date = forms.DateField(required=True,label='تاريخ بدايةالجولة', widget=widgets.DateInput(attrs={'type':'date', 'id':"start"}))
    tour_duration = forms.IntegerField(required=True,label='عدد ايام الجولة', widget=widgets.NumberInput(attrs={'class':'form-control', 'id':'tour-days'}))  
    expected_end_tour = forms.CharField(required=True,label='تاريخ نهاية الجولة المتوقع', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'end'}))
    


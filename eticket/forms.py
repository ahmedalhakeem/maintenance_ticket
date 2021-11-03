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
    



# class TicketForm(ModelForm):
#     class Meta:
#         model = Tickets
#         fields = ['ticket_type', 'ticket_priority', 'ticket_status', 'title', 'description', 'employee', 'it_user']
class Ticket_Form(forms.Form):
    tour_type = forms.ChoiceField(label='نوع الجولة', widget=forms.Select(attrs={'class':'form-control'}), choices=[('internal', 'داخلية'),('external','خارجية')])
    tour_name = forms.ModelChoiceField(label="اختر اسم الجولة", widget= forms.Select(attrs={'class': 'form-control'}), queryset=Tour_Name.objects.all())
    tour_date = forms.DateField(label='تاريخ الجولة', widget=widgets.DateInput(attrs={'type':'date'}))
    

#class Tech_issuesForm(forms.Form):
 #   p_type = forms.ModelChoiceField(label="المشكلة", required=True,queryset=ProblemType.objects.all(), widget=forms.Select(attrs={'class': 'form-control',}))
  #  user = forms.ModelChoiceField(label="اسم المستخدم", required=True, queryset=User.objects.all(), widget=forms.Select(attrs={'class':'form-control', }))





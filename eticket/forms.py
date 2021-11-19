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
    tour_duration = forms.IntegerField(required=True,label='عدد ايام الجولة', widget=widgets.NumberInput(attrs={'class':'form-control', 'id':'tour-days', "lang":"ar_SA" }))  
    # expected_end_tour = forms.CharField(required=False,disabled=True,label='تاريخ نهاية الجولة المتوقع', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'end'}))
    expected_end_tour = forms.DateField(required=False,label='تاريخ نهاية الجولة المتوقع', widget=widgets.DateInput(attrs={'type': 'date','class': 'form-control', 'id': 'end'}))
    
class Send_memo_confirm(forms.Form):
    memo_statue= forms.ChoiceField(required=True, label='حالة المذكرة', widget=forms.Select(attrs={'class': 'memo-select form-control'}),choices=[("memo_received", "memo received"), ("memo_not_received", "memo_not_received"),("wrong_memo", "wrong_memo")])
    notes = forms.CharField(required=False, label='ملاحطات', widget=forms.Textarea(attrs={'id': 'memos','class': 'memo-note form-control', 'placeholder': 'اكتب ملاحظات اخرى ان وجدت!'}))

class Ticket_Reply_Form(forms.Form):
    driver = forms.ModelChoiceField(required=True,  queryset=Drivers.objects.all(), label="اسم السائق", widget=forms.Select(attrs={'class':'form-control'}))
    car = forms.ModelChoiceField(required=True, label="اسم المركبة", widget=forms.Select(attrs={'class':'form-control'}), queryset=Cars.objects.all())

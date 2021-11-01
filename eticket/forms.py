from django import forms
from django.forms import ModelForm
from eticket.models import User, Department, Section, Tickets

class LoginForm(forms.Form):
    username = forms.CharField(label="",  required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username',}))
    password = forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))


class Register_empForm(forms.Form):
    first_name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name',}))
    last_name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your last name", }))
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter your email id', }))
    username = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your username',}))
    password = forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your password', }))
    pc_code = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'PC-code', }))
    department = forms.ModelChoiceField(label="", required=False, queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Select Department',})) 
    section = forms.ModelChoiceField(label="", required=True, queryset=Section.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Select Section',})) 



# class TicketForm(ModelForm):
#     class Meta:
#         model = Tickets
#         fields = ['ticket_type', 'ticket_priority', 'ticket_status', 'title', 'description', 'employee', 'it_user']
class TicketFormsss(forms.Form):
    ticket_type = forms.CharField(label="", required=True, widget=forms.Select(attrs={'class': 'form-control',}))
    ticket_priority = forms.CharField(label="", required=True, widget=forms.Select(attrs={'class': 'form-control',}))
    ticket_status = forms.CharField(label="", required=True, widget=forms.Select(attrs={'class':'form-control',}))
    title = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ticket title', })) 
    description= forms.CharField(label="", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Enter details if any',}))
    #date = forms.DateField(label="", widget=forms.DateTimeField())
    employee = forms.ModelChoiceField(label="", required=True, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control',}))
    it_user = forms.ModelChoiceField(label="", required=False, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control',}))
      

#class Tech_issuesForm(forms.Form):
 #   p_type = forms.ModelChoiceField(label="المشكلة", required=True,queryset=ProblemType.objects.all(), widget=forms.Select(attrs={'class': 'form-control',}))
  #  user = forms.ModelChoiceField(label="اسم المستخدم", required=True, queryset=User.objects.all(), widget=forms.Select(attrs={'class':'form-control', }))




from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Section(models.Model):
   section_name = models.CharField(max_length=64, null=True, blank=True)

   def __str__(self):
      return f"{self.id} ,{self.section_name}"

class Department(models.Model):
   department_name = models.CharField(max_length=64, null=True, blank=True)
   section = models.ManyToManyField(Section, related_name="sections", blank=True, verbose_name="الشعب")

   def __str__(self):
      return f"{self.department_name}"

class User(AbstractUser):
   department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="dept_name", default=None, null=True)
   section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="sect_name", default=None, null=True) 
   # pc_code = models.CharField(max_length=10, null=True, blank=True)

class Tour_Name(models.Model):
   tour_name = models.CharField(max_length=100, null=True, blank=True)
   
   def __str__(self):
      return f"{self.tour_name}"

class Tickets(models.Model):
   employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
   tour_type = models.CharField(max_length=20, choices=[('internal', 'internal'),('external','external')] ,null=True, blank=True)
   tour_name = models.ForeignKey(Tour_Name, on_delete=models.CASCADE, related_name='tourname', null=True, blank=True)
   tour_date = models.DateField(auto_now_add=False, null=True)
   memorandum = models.CharField(max_length=100, null=True, blank=True)
   status = models.BooleanField(default=False)
   ticket_date = models.DateField(auto_now_add=True)


   def __str__(self):
      return f" {self.id}, {self.employee}, {self.tour_type}, {self.tour_date}, {self.memorandum} "


class Drivers(models.Model):
   driver_name= models.CharField(max_length=100, null=True, blank=True)
   
   def __str__(self):
      return f"{self.driver_name}"

class Cars(models.Model):
   car_type = models.CharField(max_length=100, blank=True, null=True)

   def __str__(self):
      return f"{self.car_type}"
class Ticket_Reply(models.Model):
   ticket = models.ForeignKey(Tickets, on_delete= models.CASCADE, related_name='tickets')
   driver_name = models.ForeignKey(Drivers, on_delete=models.CASCADE, blank=True, null=True, related_query_name="drivers")
   car= models.ForeignKey(Cars, on_delete=models.CASCADE,related_name="cars")
   notes = models.CharField(max_length=100, blank=True, null=True)
   memorandum_statue = models.CharField(max_length=20, choices=[('memo_received', "memo received"), ('memo_not_received', 'memo_not_received'), ('wrong_memo', 'wrong_memo')], default=False)
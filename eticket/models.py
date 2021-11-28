from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls.base import translate_url

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
   def __str__(self):
      return f'{self.username}'

class Tickets(models.Model ):
   employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
   tour_type = models.CharField(max_length=20, choices=[('internal', 'داخلية'),('external','خارجية')] ,null=True, blank=True)
   tour_name = models.CharField(max_length=100,null=True, blank=True)
   tour_date = models.DateField(auto_now_add=False, null=True)
   tour_duration = models.IntegerField(default=1, blank=True, null=True)
   unallocated_days = models.IntegerField(default=1, blank=True, null=True)
   expected_end_tour = models.DateField(auto_now_add=False, blank=True, null=True)
   memorandum = models.CharField(max_length=100, null=True, blank=True)
   status = models.BooleanField(default=False)
   ticket_date = models.DateField(auto_now_add=True)
   notes = models.CharField(max_length=100, null=True, blank=True)


   def __str__(self):
      return f" {self.id}, {self.employee}, {self.tour_type}, {self.tour_date}, {self.memorandum}, {self.expected_end_tour}, {self.unallocated_days} "


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
   notes = models.CharField(max_length=100, blank=True, null=True)
   memorandum_statue = models.CharField(max_length=30, choices=[('تم الاستلام', "تم الاستلام"), ('لم يتم استلام المذكرة', 'لم يتم استلام المذكرة'), ('خطأ في المذكرة', 'خطأ في المذكرة')], default=False)

class Allocation(models.Model):
   reply= models.ForeignKey(Ticket_Reply, on_delete=models.CASCADE, related_name='tick_reply', blank=True, null=True)
   driver_name = models.ForeignKey(Drivers, on_delete=models.CASCADE, blank=True, null=True, related_query_name="drivers")
   car= models.ForeignKey(Cars, on_delete=models.CASCADE,related_name="cars", null=True, blank=True)
   allocate_date = models.DateField(auto_now_add=False, blank=True, null=True)
   state = models.BooleanField(default=False)
   allocation_time = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return f" {self.allocation_time}"

from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[
    path("", views.index, name="index"),
    path("login_master", views.login_master, name="login_master"),
    path("logout_page", views.logout_page, name="logout_page"),
    path("register_emp", views.register_emp, name="register_emp"),
    path("register_maintenance/", views.register_maintenance, name="register_maintenance"),
    path("employee/<int:user_id>", views.employee, name="employee"),
    path("convert_ticket/", views.convert_ticket, name="convert_ticket")
    
    # path("profile_emp/<int:emp_id>", views.profile_emp, name="profile_emp"),
    # path("manager_profile/<int:user_id>", views.manager_profile, name="manager_profile"),
    # path("it_profile/<int:user_id>", views.it_profile, name="it_profile"),
    # path("dept_mgr_profile/<int:user_id>", views.dept_mgr_profile, name="dept_mgr_profile"),
    # path("sec_mgr_profile/<int:user_id>", views.sec_mgr_profile, name="sec_mgr_profile"),

    # API routes
    # path("profile_emp/<int:emp_id>/tickets", views.tickets, name="tickets"),
    # path("sec_mgr_profile/<int:user_id>/convert_ticket", views.convert_ticket, name="convert_ticket"),
    # path("it_profile/<int:user_id>/submit_ticket", views.submit_ticket, name='submit_ticket')
]

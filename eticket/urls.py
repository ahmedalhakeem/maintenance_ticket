from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[
    path("", views.index, name="index"),
    path("login_master/", views.login_master, name="login_master"),
    path("logout_page", views.logout_page, name="logout_page"),
    path("register_emp", views.register_emp, name="register_emp"),
    path("register_maintenance/", views.register_maintenance, name="register_maintenance"),
    path("employee/<int:user_id>", views.employee, name="employee"),
    path("convert_ticket/", views.convert_ticket, name="convert_ticket"),
    path("allocate_tour/<int:tour_id>", views.allocate_tour, name="allocate_tour"),
    path('get_allocations', views.get_allocations, name="get_allocations"),
    path("send_memo_status/<int:id>", views.send_memo_status, name="send_memo_status"),
    path('allocate_per_day/<int:id>', views.allocate_per_day, name='allocate_per_day'),
    path("check_allocation_status/<int:id>", views.check_allocation_status, name="check_allocation_status"),
    path('show_replied_ticket/<int:id>', views.show_replied_ticket, name='show_replied_ticket'),
    path('show_pdf/<int:id>', views.show_pdf, name='show_pdf'),
    path('specify_period', views.specify_period, name="specify_period"),
    path('show_specified/', views.show_specified, name="show_specified"),
    path('get_sections/', views.get_sections, name="get_sections"),
    path('get_all_non_dept_sections/', views.get_all_non_dept_sections, name="get_all_non_dept_sections"),
    path('add_car/', views.add_car, name='add_car'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('done_tickets/', views.done_tickets, name='done_tickets')
    # path('reply_ticket/', views.reply_ticket, name="reply_ticket")
    
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

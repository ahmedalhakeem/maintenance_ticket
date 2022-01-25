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
    path('done_tickets', views.done_tickets, name='done_tickets'),
    path('view_allocations/<int:ticket_id>', views.view_allocations, name="view_allocations"),
    path('edit_allocated_saved/<int:id>', views.edit_allocated_saved, name='edit_allocated_saved'),
    path('ticket_info/<int:id>', views.ticket_info, name="ticket_info")
    # path('display_allocations', views.display_allocations, name="display_allocations")
]

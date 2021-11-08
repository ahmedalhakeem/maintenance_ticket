from django.contrib import admin
from .models import *

#Register 
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Section)
admin.site.register(Tickets)
admin.site.register(Ticket_Reply)
admin.site.register(Drivers)
admin.site.register(Cars)
admin.site.register(Allocation)

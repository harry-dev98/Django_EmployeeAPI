from django.contrib import admin

from .models import Employee

'''
    registering employee model with admin view
    hence be accesed/modified via admin panel.
'''
admin.site.register(Employee) 


from django.urls import path

from .views import getToken, employee, employeeList, add # importing required views

urlpatterns = [
    path('token', getToken, name="gettoken"),
    path('change/<int:pk>', employee, name='employee'), 
    path('add', add, name='add'),
    path('emplist', employeeList, name='get')
] # routes to their coresponding views
from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Employee
# Create your views here.
class EmployeeCreate(CreateView, RedirectView):
    model = Employee
    fields = ['name', 'salary']
    template_name = "home.html"

class EmployeeList(ListView):
    model = Employee
    template_name = "detail.html"

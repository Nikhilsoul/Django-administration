from django.http import HttpResponse
from employeesApp.models import Employee
from django.shortcuts import render, get_object_or_404

def employee_details(request, id):
    employee = get_object_or_404(Employee, id=id)
    context = {
        'employee': employee
    }
    return render(request, 'employee_details.html', context)

def home(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'home.html', context)
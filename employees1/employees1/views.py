from django.http import HttpResponse
from employeesApp.models import Employee
from .forms import EmployeeForm
from django.shortcuts import render, get_object_or_404

def employee_details(request, id):
    employee = get_object_or_404(Employee, id=id)
    context = {
        'employee': employee
    }
    return render(request, 'employee_details.html', context)


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form = EmployeeForm()
    #print(form)
    context = {
        'form': form
    }
    return render(request, 'add_employee.html', context)


def home(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'home.html', context)


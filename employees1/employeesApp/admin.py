from django.contrib import admin
from .models import Departments, Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'designation', 'salary', 'joining_date', 'is_active', 'department', 'manager')
    list_filter = ('designation','department')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Departments)
admin.site.register(Employee, EmployeeAdmin)
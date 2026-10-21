from django.contrib import admin
from .models import Departments, Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','full_name', 'email', 'designation', 'salary', 'joining_date', 'is_active', 'department', 'manager')
    list_filter = ('designation','department')
    search_fields = ('full_name', 'email')
    list_editable = ('is_active','salary')
    list_display_links = ('full_name', 'email')
    ordering = ('id',)


admin.site.register(Departments)
admin.site.register(Employee, EmployeeAdmin)
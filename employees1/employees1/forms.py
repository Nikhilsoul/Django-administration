from django import forms
from employeesApp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        Widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }
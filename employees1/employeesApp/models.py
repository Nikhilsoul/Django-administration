from django.db import models

# Create your models here.

class Departments(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.location}"

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    designation = models.CharField(choices=[('Manager', 'Manager'), ('Developer', 'Developer'), ('Designer', 'Designer')], max_length=20)
    salary = models.IntegerField()
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, blank=True, null= True)
    manager = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
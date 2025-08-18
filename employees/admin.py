from django.contrib import admin
from .models import Employees
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','email','contact']
    
admin.site.register(Employees,EmployeeAdmin)
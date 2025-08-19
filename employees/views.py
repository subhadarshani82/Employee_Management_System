from django.shortcuts import render,redirect
from . models import Employees
from django.contrib import messages
import re
# Create your views here.
def add_employee(request):
    if request.method=='POST':
        name=request.POST.get('name').strip()
        email=request.POST.get('email').strip()
        phone=request.POST.get('contact').strip()
        
        #validation 
        if not name or not re.fullmatch(r'[A-Za-z ]+',name):
            messages.error(request,"Name can not be blank and it should contain only Alphabets and Space.")
        elif not name or not re.fullmatch(r'[^@]+@[^@]+\.[^@]+',email):
            messages.error(request,"Email should be valid email.")
        elif not phone.isdigit() or len(phone)!=10 :
            messages.error(request,"Mobile no should be of 10 digits.")
        else:
            print(name,email,phone)
            employees=Employees(name=name,email=email,contact=phone)
            employees.save()
            messages.success(request,"Employee added Successfully.")
        return render(request,'list_employees.html')
        # return redirect('add_employee')#change it later
        
    return render(request,'list_employees.html')
from django.shortcuts import render,redirect
from . models import Employees
from django.contrib import messages
import re
from django.db.models import Q
# Create your views here.

def list_employee(request):
    query=request.GET.get('query',"").strip()
    edit_id=request.GET.get('edit')
    # print(query)
    employees=Employees.objects.all() 
    # print(employees)
    if 'query' in request.GET:
        if query=="":
            messages.error(request,'Please provide value to search.',extra_tags='search')
        else:
            employees= Employees.objects.filter(
                Q(name__icontains=query)| Q(email__icontains=query)| Q(contact__icontains=query)
            )
            if not employees.exists():
                messages.warning(request,'No matching Employee found.',extra_tags='search')
    employee=None
    if edit_id:
        try:
            employee= Employees.objects.get(id=edit_id)
        except Employees.DoesNotExist:
            messages.error(request,'Employee not found.',extra_tags='modal')
    return render(request,'list_employees.html',{'employees':employees,'employee':employee})
    
def add_employee(request):
    if request.method=='POST':
        name=request.POST.get('name').strip()
        email=request.POST.get('email').strip()
        mobile=request.POST.get('contact').strip()
        
        #validation 
        if not name or not re.fullmatch(r'[A-Za-z ]+',name):
            messages.error(request,"Name can not be blank and it should contain only Alphabets and Space.",extra_tags='modal')
            return redirect('/list_employee/?modal=add')
        elif not email or not re.fullmatch(r'[^@]+@[^@]+\.[^@]+',email):
            messages.error(request,"Email should be valid email.",extra_tags='modal')
            return redirect('/list_employee/?modal=add')
        elif not mobile.isdigit() or len(mobile)!=10 :
            messages.error(request,"Mobile no should be of 10 digits.",extra_tags='modal')
            return redirect('/list_employee/?modal=add')
        else:
            # print(name,email,mobile)
            employees=Employees(name=name,email=email,contact=mobile)
            employees.save()
            messages.success(request,"Employee added Successfully.",extra_tags='modal')
            return redirect('/list_employee/?modal=add')

    return redirect('list_employee')

def update_employee(request,id):
    employee=Employees.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name').strip()
        email=request.POST.get('email').strip()
        mobile=request.POST.get('contact').strip()
        
        #validation 
        if not name or not re.fullmatch(r'[A-Za-z ]+',name):
            messages.error(request,"Name can not be blank and it should contain only Alphabets and Space.",extra_tags='modal')
            return redirect(f'/list_employee/?edit={id}')
        elif not name or not re.fullmatch(r'[^@]+@[^@]+\.[^@]+',email):
            messages.error(request,"Email should be valid email.",extra_tags='modal')
            return redirect(f'/list_employee/?edit={id}')
        elif not mobile.isdigit() or len(mobile)!=10 :
            messages.error(request,"Mobile no should be of 10 digits.",extra_tags='modal')
            return redirect(f'/list_employee/?edit={id}')
        else:
            
            employee.name=name
            employee.email=email
            employee.contact=mobile
            employee.save()
            messages.success(request,f"Employee {employee.name} updated Successfully.",extra_tags='modal')
            return redirect(f'/list_employee/?edit={id}')
            
        

    return redirect('list_employee')

def delete_employee(request,id):
    employee=Employees.objects.get(id=id)
    employee.delete()
    return redirect('list_employee')


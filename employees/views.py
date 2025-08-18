from django.shortcuts import render

# Create your views here.
def add_employee(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('contact')
        print(name,email,phone)
    return render(request,'list_employees.html')
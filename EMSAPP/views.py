from django.shortcuts import render, redirect
from .models import Employee

def employee_list(request):
    data = Employee.objects.all()
    return render(request, 'EMSAPP/list.html', {'data' : data})

def add_employee(request):
    if request.method == 'POST':
        Employee.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            department = request.POST['department'],
            salary = request.POST['salary'],
        )
        return redirect('employee_list')
    return render(request, 'EMSAPP/add.html')

def delete_employee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('employee_list')

def update_employee(request, id):
    emp =  Employee.objects.get(id=id)

    if request.method == 'POST':
        emp.name = request.POST['name']
        emp.email = request.POST['email']
        emp.department = request.POST['department']
        emp.salary = request.POST['salary']
        emp.save()
        return redirect('employee_list')
    return render(request, 'EMSAPP/update.html',{'emp' : emp})
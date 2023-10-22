from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee


# This function will add new employee and show employees
def add_show(request):
    if request.method == 'POST':
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            salary = fm.cleaned_data['salary']
            department = fm.cleaned_data['department']
            phone_number = fm.cleaned_data['phone_number']
            reg = Employee(name=name, email=email, salary=salary, department=department, phone_number=phone_number)
            reg.save()
            # fm.save()

        # Generally we render the success message page here, but for now we are returning the new form only
        fm = EmployeeForm()
    else:
        fm = EmployeeForm()

    emp = Employee.objects.all().order_by('id')
    paginator = Paginator(emp, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'employee/addandshow.html', {'form': fm, 'emp': page_obj})


# this function will delete the employee
def delete_emp(request, id):
    if request.method == "POST":
        deleted_emp = Employee.objects.get(pk=id)
        deleted_emp.delete()

    return HttpResponseRedirect('/')


# this function will update and edit
def update_emp(request, id):
    if request.method == "POST":
        emp = Employee.objects.get(pk=id)
        fm = EmployeeForm(request.POST, instance=emp)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        emp = Employee.objects.get(pk=id)
        fm = EmployeeForm(instance=emp)

    return render(request, 'employee/updateemployee.html', {'form': fm})

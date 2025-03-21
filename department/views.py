from django.shortcuts import render , redirect

from django.contrib import messages
from  .models import * 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
# Create your views here.
def add_department(request):
    if request.method == "POST":
        name = request.POST.get('name')
        department_id = request.POST.get('department_id')
        section = request.POST.get('section')

    

        # Save department information
        department = Department.objects.create(
            name= name,
            department_id= department_id,
            section = section,
        )
        messages.success(request, "Department added Successfully")
        # return render(request, "department_list")

  

    return render(request,"departments/add-departments.html")
def department_list(request):
    department_list = Department.objects.all()
    unread_notification = request.user.notification_set.filter(is_read=False)
    context = {
        'department_list': department_list,
        'unread_notification': unread_notification
    }
    return render(request, "departments/departments.html", context)
# Create your views here.

def view_department(request, slug):
    department = get_object_or_404(Department, department_id= slug)
    context = {
        'department': department
    }
    return render(request, "departments/department-details.html", context)

def edit_department(request, slug):
    department = get_object_or_404(Department, department_id=slug)
    if request.method == "POST":
        name = request.POST.get('name')
        department_id = request.POST.get('department_id')
        section = request.POST.get('section')
        
        #update department information
        department.name = name
        department.department_id = department_id
        department.section = section
        department.save()
        
        
        return redirect('department_list')
    return render(request, "departments/edit-departments.html", {'department': department})

def delete_department(request, slug):
    if request.method == 'POST':
        department = get_object_or_404(Department, department_id=slug)
        department_name = f"{department.name}"
        department.delete()
        create_notification(request.user, f"Deleted department: {department_name}") # type: ignore
        return redirect('department_list')
    return HttpResponseForbidden()        
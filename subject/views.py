from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .models import *
from django.http import HttpResponseForbidden
from department.models import Department
from teacher.models import Teacher
# Create your views here.
def add_subject(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        code=request.POST.get('code')
        description=request.POST.get('description')
        credits=request.POST.get('credits')
        
        #fetching foreignkey objects
        department=get_object_or_404(Department, id=request.POST.get('department'))
        teacher=get_object_or_404(Teacher, id=request.POST.get('teacher'))

        #save subject
        subject=Subject.objects.create(
            name=name,
            code=code,
            description=description,
            department=department,
            credits=credits
        )
        #link teacher to subject
        TeacherSubject.objects.create(teacher=teacher, subject=subject)


        messages.success(request, 'Subject added successfully')
        #return redirect('subject_list')
    departments = Department.objects.all()
    return render(request, 'subjects/add-subject.html', {'departments': departments})

def subject_list(request):
    subject_list = Subject.objects.all()
    unread_notification = request.user.notification_set.filter(is_read=False)
    context = {
        'subject_list': subject_list,
        'unread_notification': unread_notification
    }
    return render(request, 'subjects/subjects.html', context)

def view_subject(request, slug):
    subject = get_object_or_404(Subject, subject_id=slug)
    context = {
        'subject': subject
    }  
    return render(request, 'subjects/subject-details.html', context)


def edit_subject(request, slug):
    subject= get_object_or_404(Subject, slug=slug)
    if request.method=='POST':
        name=request.POST.get('name')
        code=request.POST.get('code')
        description=request.POST.get('description')
        credits=request.POST.get('credits')

         #fetching foreignkey objects
        department=get_object_or_404(Department, id=request.POST.get('department'))
        teacher=get_object_or_404(Teacher, id=request.POST.get('teacher'))


        #save subject information
        subject.name=name
        subject.code=code
        subject.description=description
        subject.department=department
        subject.credits=credits
        subject.save()

        return redirect('subject_list')
    departments = Department.objects.all()
    return render(request, 'subjects/add-subject.html', {'departments': departments})

def delete_subject(request, slug):
    if request.method=='POST':
        subject= get_object_or_404(Subject, slug=slug)
        subject_name = f"{subject.name} {subject.code}"
        subject.delete()

        return redirect('subject_list')
    return HttpResponseForbidden()
from django.shortcuts import render, redirect
from django.contrib import messages
from  .models import * 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden

# Create your views here.
def add_teacher(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_id=request.POST.get('teacher_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        section = request.POST.get('section')

    

        # Save teacher information
        teacher = Teacher.objects.create(
            first_name= first_name,
            last_name= last_name,
            teacher_id = teacher_id,
            gender= gender,
            date_of_birth= date_of_birth,
            religion= religion,
            joining_date= joining_date,
            mobile_number = mobile_number,
            section = section,
        )
        messages.success(request, "Teacher added Successfully")
        # return render(request, "teacher_list")

  

    return render(request,"teachers/add-teacher.html")
def teacher_list(request):
    teacher_list = Teacher.objects.all()
    unread_notification = request.user.notification_set.filter(is_read=False)
    context = {
        'teacher_list': teacher_list,
        'unread_notification': unread_notification
    }
    return render(request, "teachers/teachers.html", context)

def view_teacher(request, slug):
    teacher = get_object_or_404(Teacher, teacher_id = slug)
    context = {
        'teacher': teacher
    }
    return render(request, "teachers/teacher-details.html", context)

def edit_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_id = request.POST.get('teacher_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        section = request.POST.get('section')

    #update teacher info
        teacher.first_name = first_name
        teacher.last_name = last_name
        teacher.teacher_id = teacher_id
        teacher.gender= gender
        teacher.date_of_birth= date_of_birth
        teacher.religion= religion
        teacher.joining_date= joining_date
        teacher.mobile_number = mobile_number
        teacher.section = section
        teacher.save()
        
        return redirect('teacher_list')
    return render(request, "teachers/edit-teacher.html", {'teacher': teacher})

def delete_teacher(request, slug):
    if request.method == 'POST':
        teacher = get_object_or_404(Teacher, slug=slug)
        teacher_name = f"{teacher.first_name} {teacher.last_name}"
        teacher.delete()
        return redirect ('teacher_list')
    return HttpResponseForbidden()
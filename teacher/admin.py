from django.contrib import admin
from .models import Teacher

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender','teacher_id' ,'date_of_birth', 'religion', 'joining_date', 'mobile_number', 'section')
    search_list = ('first_name', 'last_name','teacher_id','section')
    list_filter=('teacher_id','section')
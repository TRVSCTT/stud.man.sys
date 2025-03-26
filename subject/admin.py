from django.contrib import admin
from .models import Subject , TeacherSubject 
# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'department', 'credits']
    search_fields = ['name', 'code']
    list_filter = ['code']

@admin.register(TeacherSubject)
class TeacherSubjectAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'subject']
    search_fields = ['teacher', 'subject']
    list_filter = ['teacher']
 

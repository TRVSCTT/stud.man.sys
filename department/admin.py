from django.contrib import admin
from .models import Department
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department_id', 'section')
    search_list = ( 'name','department_id','section')
    list_filter= ('department_id','section')
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify
# Create your models here.
class Subject(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    description=models.TextField(max_length=255)
    department=models.ForeignKey('department.Department',on_delete=models.CASCADE)
    credits=models.IntegerField()
    slug=models.SlugField(max_length=255,unique=True,blank=True)
     
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(f"{self.name}-{self.code}")
        super(Subject,self).save(*args, **kwargs)
    

    def __str__(self):
        return  f"{self.name} - {self.code}"
    
# TeacherSubject model that links each teacher to a subject
class TeacherSubject(models.Model):
    teacher=models.ForeignKey('teacher.Teacher',on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.teacher} - {self.subject}"
    
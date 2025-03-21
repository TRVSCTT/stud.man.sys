from django.db import models
from django.utils.text import slugify
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    department_id = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.department_id}")
        super(Department, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}  ({self.department_id})"
# Create your models here.

from django.contrib import admin
from django_students import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Course)
admin.site.register(models.Teacher)
admin.site.register(models.Lessons)
admin.site.register(models.Grade)
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator, FileExtensionValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=600)

    class Meta:
        app_label = "django_students"
        ordering = ("name",)
        verbose_name = "Курс"

    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    name = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="Аноним",
        verbose_name="Пользователь",
        max_length=200
    )
    surname = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    course = models.ForeignKey(to=Course,
                               on_delete=models.SET_NULL,
                               null=True)

    class Meta:
        app_label = "django_students"
        ordering = ("surname", "name")
        verbose_name = "Студенты"

    def __str__(self):
        return f"{self.surname} {self.name} {self.email} {self.course}"

class Teacher(models.Model):
    name = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="Аноним",
        verbose_name="Пользователь",
        max_length=200
    )
    surname = models.CharField(max_length=200)
    job_title = models.CharField(max_length=500)
    email = models.CharField(max_length=200)


    class Meta:
        app_label = "django_students"
        ordering = ("surname", "name")
        verbose_name = "Преподаватели"

    def __str__(self):
        return f"{self.surname} {self.name} {self.job_title} {self.email}"



class Lessons(models.Model):
    name = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="Аноним",
        verbose_name="Пользователь",
        max_length=200
    )
    course = models.ForeignKey(to=Course,
                               on_delete=models.SET_NULL,
                               null=True)
    teacher = models.ForeignKey(to=Teacher,
                                on_delete=models.SET_NULL,
                                null=True)
    date = models.DateTimeField()
    classroom = models.IntegerField(null=False)



    class Meta:
        app_label = "django_students"
        ordering = ("name",)
        verbose_name = "Занятия"

    def __str__(self):
        return f"{self.name} {self.teacher}"


class Grade(models.Model):
    student = models.ForeignKey(to=Student,
                                on_delete=models.SET_NULL,
                                null=True)
    grade = models.IntegerField
    course = models.ForeignKey(to=Course,
                               on_delete=models.SET_NULL,
                               null=True)

    class Meta:
        app_label = "django_students"
        verbose_name = "Оценка"

    def __str__(self):
        return f"{self.grade} {self.student}"
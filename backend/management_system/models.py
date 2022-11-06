from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Student(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)


class Subject(models.Model):
    title = models.CharField(max_length=63)
    default_first_semester_duration = models.IntegerField(default=13)
    default_second_semester_duration = models.IntegerField(default=15)
    default_lesson_rate = models.IntegerField()


class Group(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    first_semester_duration = models.IntegerField()
    second_semester_duration = models.IntegerField()
    lesson_rate = models.IntegerField()


class StudentXGroup(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

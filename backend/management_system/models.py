from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Student(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Subject(models.Model):
    title = models.CharField(max_length=63, unique=True)
    default_first_semester_duration = models.IntegerField(default=13)
    default_second_semester_duration = models.IntegerField(default=15)
    default_lesson_rate = models.IntegerField()

    def __str__(self):
        return self.title


class Semester(models.Model):
    year = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f"Semester({self.year}#{self.number})"


class Group(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    duration = models.IntegerField()
    lesson_rate = models.IntegerField()


class StudentXGroup(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, Subject, Group, Application, StudentXGroup

admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Group)
admin.site.register(Application)
admin.site.register(StudentXGroup)

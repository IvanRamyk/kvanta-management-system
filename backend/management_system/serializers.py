from django.contrib.auth import get_user_model
from rest_framework import serializers

from management_system.models import Student, Subject, Semester, Group, Application


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "parent",
            "first_name",
            "last_name",
        )


class StudentDetailedSerializer(StudentSerializer):
    parent = UserSerializer(many=False)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            "id",
            "title",
            "default_first_semester_duration",
            "default_second_semester_duration",
            "default_lesson_rate",
        )


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ("id", "year", "number")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("subject", "semester", "name", "duration", "lesson_rate")


class GroupDetailedSerializer(GroupSerializer):
    subject = SubjectSerializer(many=False)
    semester = SemesterSerializer(many=False)


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ("student", "subject")


class ApplicationDetailedSerializer(ApplicationSerializer):
    student = StudentSerializer(many=False)
    subject = SubjectSerializer(many=False)

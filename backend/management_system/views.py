from django.contrib.auth import get_user_model
from rest_framework import viewsets

from management_system.models import Student, Subject, Semester, Group, Application
from management_system.serializers import (
    UserSerializer,
    StudentDetailedSerializer,
    StudentSerializer,
    SubjectSerializer,
    SemesterSerializer,
    GroupDetailedSerializer,
    GroupSerializer,
    ApplicationDetailedSerializer,
    ApplicationSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentDetailedSerializer
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return StudentDetailedSerializer
        return StudentSerializer

    def get_queryset(self):
        queryset = self.queryset
        parent_id = self.request.query_params.get('parent')
        if parent_id is not None:
            queryset = queryset.filter(parent__pk=parent_id)
        return queryset


class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SemesterViewSet(viewsets.ModelViewSet):
    serializer_class = SemesterSerializer
    queryset = Semester.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupDetailedSerializer
    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return GroupDetailedSerializer
        return GroupSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationDetailedSerializer
    queryset = Application.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ApplicationDetailedSerializer
        return ApplicationSerializer

    def get_queryset(self):
        queryset = self.queryset
        parent_id = self.request.query_params.get('parent')
        if parent_id is not None:
            queryset = queryset.filter(student__parent__pk=parent_id)
        return queryset

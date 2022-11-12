from management_system.views import (
    UserViewSet,
    StudentViewSet,
    SubjectViewSet,
    SemesterViewSet,
    GroupViewSet,
    ApplicationViewSet,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("students", StudentViewSet, basename="student")
router.register("subjects", SubjectViewSet, basename="subject")
router.register("semesters", SemesterViewSet, basename="semester")
router.register("groups", GroupViewSet, basename="group")
router.register("applications", ApplicationViewSet, basename="application")

urlpatterns = router.urls

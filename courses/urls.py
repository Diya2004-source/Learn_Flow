from django.urls import path,include
from .views import CourseViewSet,LessonViewSet,ModuleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'Course',CourseViewSet)
router.register(f'Lesson',LessonViewSet)
router.register(f'Module',ModuleViewSet)


urlpatterns = [
    path('',include(router.urls))
]
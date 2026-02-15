from django.apps import AppConfig
from django.urls import path,include
from .views import LessonProgressViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'LessonProgress',LessonProgressViewSet)

urlpatterns = [
    path('',include(router.urls))
]
class ProgressConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'progress'

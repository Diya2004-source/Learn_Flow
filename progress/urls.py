from django.urls import path,include
from .views import LessonProgressViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'LessonProgress',LessonProgressViewSet)

urlpatterns = [
    path('',include(router.urls))
]
from django.apps import AppConfig
from django.urls import path,include
from .views import CertificateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'Certificate',CertificateViewSet)

urlpatterns = [
    path('',include(router.urls))
]

class CertificateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'certificate'

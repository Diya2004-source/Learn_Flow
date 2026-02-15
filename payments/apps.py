from django.apps import AppConfig
from django.urls import path,include
from .views import PaymentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'Payment',PaymentViewSet)

urlpatterns = [
    path('',include(router.urls))
]
class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments'

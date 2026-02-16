from django.urls import path,include
from .views import PaymentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'Payment',PaymentViewSet)

urlpatterns = [
    path('',include(router.urls))
]
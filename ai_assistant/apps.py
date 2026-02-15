from django.apps import AppConfig
from django.urls import path,include
from .views import ChatMessageViewSet,ChatSessionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'ChatMessage',ChatMessageViewSet)
router.register(f'ChatSession',ChatSessionViewSet)

urlpatterns = [
    path('',include(router.urls))
]

class AiAssistantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai_assistant'

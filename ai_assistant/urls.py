from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatMessageViewSet, ChatSessionViewSet

router = DefaultRouter()
router.register('chat-messages', ChatMessageViewSet)
router.register('chat-sessions', ChatSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

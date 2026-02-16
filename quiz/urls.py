from django.urls import path,include
from .views import QuestionViewSet,QuizAttemptViewSet,QuizViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'Quiz',QuizViewSet)
router.register(f'Question',QuestionViewSet)
router.register(f'QuizAttempt',QuizAttemptViewSet)

urlpatterns = [
    path('',include(router.urls))
]
from django.shortcuts import render
from rest_framework import viewsets
from .models import Quiz,Question,QuizAttempt
from .serializers import QuestionSerializer,QuizAttemptSerializer,QuizSerializer

# Create your views here.
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer
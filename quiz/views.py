from django.shortcuts import render
from rest_framework import viewsets
from .models import Quiz,Question,QuizAttempt
from .serializers import QuestionSerializer,QuizAttemptSerializer,QuizSerializer

# Create your views here.
class QuizViewSet(viewsets.ModelViewSet):
    viewsets = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    viewsets = Question.objects.all()
    serializer_class = QuestionSerializer

class QuizAttemptViewSet(viewsets.ModelViewSet):
    viewsets = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer
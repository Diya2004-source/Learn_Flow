from django.shortcuts import render
from rest_framework import viewsets
from .models import LessonProgress
from .serializers import LessonProgressSerializer

# Create your views here.
class LessonProgressViewSet(viewsets.ModelViewSet):
    queryset = LessonProgress.objects.all()
    serializer_class = LessonProgressSerializer


from django.shortcuts import render
from rest_framework import viewsets
from .models import Course,Module,Lesson
from .serializers import CourseSerializer,ModuleSerializer,LessonSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class CourseListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({
            "message": "Only logged in user can see this"
        })

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    
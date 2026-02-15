from django.shortcuts import render
from rest_framework import viewsets
from .models import ChatMessage,ChatSession
from .serializers import ChatMessageSerializer,ChatSessionSerializer

# Create your views here.
class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

class ChatSessionViewSet(viewsets.ModelViewSet):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer
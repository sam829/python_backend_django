from django.shortcuts import render
from rest_framework import viewsets
from .models import Notes
from .serializers import NotesSerializer

# Create your views here.
class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()

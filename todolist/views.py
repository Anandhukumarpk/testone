from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TodoSereializer
from .models import todo

class TodoViewsets(viewsets.ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSereializer

    

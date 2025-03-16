from django.shortcuts import render
from api.models import Book
from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookSerializer
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    pass
from django.shortcuts import render
from rest_framework import generics
from .models import Author , Book
from .serializers import BookSerializer , AuthorSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import serializers
from rest_framework import filters

#["ListView", "DetailView", "CreateView", "UpdateView", "DeleteView"]
class Book_List_View(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   
    filterset_fields = ['title', 'author', 'publication_year']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']

class Book_Retrieve_View(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Book_Create_View(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()   
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError(f'Book with title "{title}" already exists')
        else:
            serializer.save()

class Book_Update_View(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def perform_update(self, data, serializer):
        if len (data['title']) == 0:
            raise serializers.ValidationError('Title cannot be empty')
        else:
            serializer.save()

    

class Book_Delete_View(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def perform_destroy(self, instance):
        instance.delete()

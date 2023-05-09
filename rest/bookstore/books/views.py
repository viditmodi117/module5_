from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from books.models import Book
from books.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
def api(request):
    return render(request, 'api.html')
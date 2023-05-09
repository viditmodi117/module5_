from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from books.views import BookViewSet


router = routers.DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]
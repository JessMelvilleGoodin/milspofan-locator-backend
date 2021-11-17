from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, generics

# Create your views here.

class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
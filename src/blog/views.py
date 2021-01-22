from django.shortcuts import render
from rest_framework import generics
from .models import Category, Post
from .serializers import PostSerializer, PostDetailSerializer


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.ListAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Category, Post, Like
from .serializers import PostSerializer, PostDetailSerializer, CommentCreateSrializer

class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"

@api_view(['POST'])
def comment_api(request, slug):
    try:
         post = get_object_or_404(Post, slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CommentCreateSerializer(post,data=request.data, context={'request':request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
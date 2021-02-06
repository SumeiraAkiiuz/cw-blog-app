from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Category, Post, Like, PostView
from .serializers import PostDetailSerializer, CommentCreateSrializer, PostUpdateSerializer, PostListSerializer, CommentSerializer
from .paginations import MyPagination
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsKeeper
from .paginations import MyPagination
from .serializers import serializers

class PostList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostListSerializer
    pagination_class = MyPagination
    queryset = Post.objects.all()

class userPostList(generics.ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated, IsKeeper]
    
    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        return queryset
    
    
class PostCreateApi(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"
    
    def get_object(self):
        obj = super().get_object()
        PostView.objects.get_or_create(user=self.request.user, post=obj)
        return obj

    
class PostUpdate(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsKeeper]
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = "slug"


class PostDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsKeeper]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = "slug"


    
class CreateCommentAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSrializer
    
    def post(self, slug):
        post = get_object_or_404(Post, slug=slug)
        serializer = CommentCreateSrializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


        
class CreateLikeAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, slug):
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
            
        data = {
            "messages": "like"
        }
        return Response(data)


    
    
# @api_view(['POST'])
# def comment_api(request, slug):
#     try:
#          post = get_object_or_404(Post, slug=slug)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = CommentCreateSerializer(post,data=request.data, context={'request':request})
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
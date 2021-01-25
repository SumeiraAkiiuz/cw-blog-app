from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category, Like, PostView

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
            'category',
            'status'
            
        )
        
class CommentCreateSrializer(serializers.ModelSerializer):
    # content = serializers.CharField()
    # user= serializers.PrimaryKeyRelatedField(source = 'user', queryset=User.objects.all(), write_only=True)
    # post = serializers.PrimaryKeyRelatedField(source = 'post', queryset=Post.objects.all(), write_only=True)
    
    class Meta:
        model = Comment
        fields = (
            "content",
        )
        
class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentCreateSrializer(many=True)
    class Meta:
        model = Post
        fields = (
            'title',
            'comment_count',
            'view_count',
            'like_count',
            'comments'
        )
        

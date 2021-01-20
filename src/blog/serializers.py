from rest_framework import serializers
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
        
        
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'comment_count',
            'view_count',
            'like_count',
            'comments'
        )
        

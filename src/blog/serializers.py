from rest_framework import serializers
from .models import Post, Comment, Category, Like

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )
        
        
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'comment_count',
            'view_count',
            'like_count',
            'comments'
        )
        
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = (
            'title',
            'content',
            'image',
            'category',
            'status',
        )
 

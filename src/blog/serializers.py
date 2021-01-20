from rest_framework import serializers
from .models import Post, Comment, Category, Like, PostView

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
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'user',
            'post',
            'time_stamp',
            'content'
        )
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'user',
            'post'
        )
 
#  class PostViewSerializer(serializers.ModelSerializer):
#      class Meta:
#          model = PostView
#          fields = (
#              'user',
#              'post',
#              'time_stamp'
#          )

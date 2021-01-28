from django.db.models import fields
from django.http import request
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category, Like, PostView
from django.db.models import Q

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
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'post',
            'time_stamp',
            'content',
        )

class CommentCreateSrializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "content",
        )
        
class PostDetailSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Post.OPTIONS)
    author = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    comments = CommentCreateSrializer(many=True)
    keeper = serializers.SerializerMethodField(read_only=True)
    url_update = serializers.HyperlinkedIdentityField(
        view_name = 'update',
        lookup_field = 'slug'
    )
    url_like = serializers.HyperlinkedIdentityField(
        view_name = 'like',
        lookup_field = 'slug'
    )
    url_delete = serializers.HyperlinkedIdentityField(
        view_name = 'delete',
        lookup_field = 'slug'
    )
    url_comment = serializers.HyperlinkedIdentityField(
        view_name = 'comment',
        lookup_field = 'slug'
    )
    
    class Meta:
        model = Post
        fields = (
            
            # 'title',
            # 'comment_count',
            # 'view_count',
            # 'like_count',
            # 'comments'
            
            'url_update',
            'url_like',
            'url_delete',
            'url_comment',
            'id',
            'title',
            'content',
            'comment_count',
            'view_count',
            'like_count',
            'comments',
            'image',
            'status',
            'publish_date',
            'last_updated',
            'author',
            'slug',
            'comment_count',
            'view_count',
            'like_count',
            'keeper',
            'liked',
        )
        
    def get_author(self, obj):
        return obj.author.username
    
    def get_keeper(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False
        
    def get_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if Post.objects.filter(Q(like__user=request.user)& Q(like__post=obj)).exists():
                return True
            return False

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    detail_url = serializers.HyperlinkedIdentityField(
        view_name= 'detail',
        lookup_field = 'slug'
    )
    
    class Meta:
        model = Post
        fields = (
            'detail_url',
            'title',
            'content',
            'image',
            'status',
            'publish_date',
            'author',
            'slug',
            'comment_count',
            'view_count',
            'like_count'
        )
        
    def get_author(self, obj):
        return obj.author.username
    
class PostUpdateSerializer(serializers.ModelSerializer):
    keeper = serializers.SerializerMethodField(read_only = True)
    
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'image',
            'status',
            'keeper',
        )
        
    def get_keeper(self, obj):
        request =  self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False
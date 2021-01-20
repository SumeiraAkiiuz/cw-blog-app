from django.shortcuts import render
from rest_framework import generics
from .models import Category, Post
from .serializers import CategorySerializer, CategoryDetailSerializer, PostSerializer


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    
    def get_queryset(self):
        queryset = Post.objects.all()
        category = self.kwargs["category"]
        queryset = queryset.filter(category__name=category)
        return queryset
    

class PostDetail(generics.ListAPIView):
    serializer_class= PostSerializer
    
    def get_queryset(self):
        queryset = Post.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(post__title=title)
        return queryset
 
def post_list(request):
    qs = Post.objects.all()
    context = {
        "object_list": qs
    }
    return render(request, "blog/post_list.html", context)


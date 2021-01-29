from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import status
from .models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer, ProfileSerializer

# Create your views here.

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
@api_view(["GET", "PUT"])
def Profile_update(request):
    if request.method == "GET":
        serializer = ProfileSerializer(request.user.profile)
        
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = ProfileSerializer(request.user.profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Profile is now updated."
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
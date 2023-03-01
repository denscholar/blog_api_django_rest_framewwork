from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


class AllPostview(APIView):
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(
            operation_summary="List all post",
            operation_description="This returns a list of all post created"
    )
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        response = {
            "message": "all post",
            "data": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
            operation_summary="Make a post"
            
    )
    def post(self, request):
        post = request.data
        serializer = PostSerializer(data=post)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "post",
                "data": serializer.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class PostDetailView(APIView):
    permission_class = [IsAuthenticated]
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)

        respose = {
            "data": serializer.data,
        }
        return Response(respose, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        data = request.data
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




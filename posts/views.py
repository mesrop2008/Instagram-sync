from django.shortcuts import render 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import SyncService
from .serializers import PostSerialiizer
from .models import Post

class SyncPostsView(APIView):
     
    def post(self, request):
        post_data = SyncService.get_posts()
        SyncService.upsert(post_data)
        return Response({"synced": len(post_data)})

class ListPostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiizer


    

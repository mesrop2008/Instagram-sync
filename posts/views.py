from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import SyncService
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class SyncPostsView(APIView):
    """Запись постов в бд"""

    def post(self, request):
        post_data = SyncService.get_posts()
        SyncService.upsert(post_data)
        return Response({"synced": len(post_data)})


class ListPostsView(generics.ListAPIView):
    """Получение постов из бд"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCommentsView(APIView):
    """Отправка комментария"""

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "post not found"}, status=404)

        try:
            data = SyncService.create_comment(post.instagram_id, request.data.get("text"))
            comment = Comment.objects.create(post=post, text=request.data.get("text"))
        except Exception:
            return Response({"error": "failed to send comment"}, status=500)
        
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import SyncService
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostSyncView(APIView):
    """Saving posts to the database"""

    def post(self, request):
        post_data = SyncService.fetch_posts_from_instagram()
        SyncService.sync_posts(post_data)
        return Response({"synced": len(post_data)})


class PostListView(generics.ListAPIView):
    """Retrieving posts from the database"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCommentCreateView(APIView):
    """Post comment"""

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "post not found"}, status=404)

        try:
            data = SyncService.post_comment_to_instagram(post.instagram_id, request.data.get("text"))
            comment = Comment.objects.create(post=post, text=request.data.get("text"))
        except Exception:
            return Response({"error": "failed to send comment"}, status=500)
        
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

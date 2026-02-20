from unittest.mock import patch
from rest_framework.test import APITestCase
from rest_framework import status
from posts.models import Post, Comment
from posts.services import SyncService

class PostCommentsTests(APITestCase):
    """Тесты создания комментариев"""

    def setUp(self):
        self.post = Post.objects.create(
            instagram_id="123",
            media_type="IMAGE",
            media_url="http://test.com/image.jpg",
            permalink="http://test.com/post",
            timestamp="2024-01-01T00:00:00"
        )

    @patch("posts.services.SyncService.create_comment")
    def test_create_comment(self, mock_create):
        """ Проверка создания комментария и ответа API"""
        mock_create.return_value = {"id": "comment_id"}

        url = f"/api/posts/{self.post.pk}/comment/"
        response = self.client.post(url, {"text": "Test comment"}, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().text, "Test comment")
        
    def test_create_comment_post_not_found(self):
        """Проверка ошибки если поста нет в бд"""

        url = f"/api/posts/999/comment/"
        response = self.client.post(url, {"text": "Test comment"}, format="json")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["error"], "post not found")
        self.assertEqual(Comment.objects.count(), 0)

    @patch("posts.services.SyncService.create_comment")
    def test_create_comment_instagram_error(self, mock_create):
        """Проверка ошибки если не получилось отправить комментарий"""

        mock_create.side_effect = Exception("Instagram error")

        url = f"/api/posts/{self.post.pk}/comment/"
        response = self.client.post(url, {"text": "Test comment"}, format="json")

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data["error"], "failed to send comment")
        self.assertEqual(Comment.objects.count(), 0)
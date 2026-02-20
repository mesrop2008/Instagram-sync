import requests

from config import settings
from posts.models import Post

ACCESS_TOKEN = settings.INSTAGRAM_ACCESS_TOKEN


class SyncService:
     """Handles Instagram API interactions and syncs posts with the local database."""

    @staticmethod
    def fetch_posts_from_instagram() -> list[dict]:
        url = (
            f"https://graph.instagram.com/me/media"
            f"?fields=id,caption,media_type,media_url,permalink,timestamp"
            f"&access_token={ACCESS_TOKEN}"
        )
        all_posts = []

        while url:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                all_posts.extend(data.get("data", []))
                url = data.get("paging", {}).get("next")
            else:
                raise Exception(f"Failed to get posts")

        return all_posts

    @staticmethod
    def sync_posts(posts_data: list[dict]) -> None:
        """Saving or deleting posts in the database"""
        instagram_ids = [post["id"] for post in posts_data]

        for post in posts_data:
            Post.objects.update_or_create(
                instagram_id=post["id"],  #using for search
                defaults={
                    "media_type": post["media_type"],
                    "media_url": post["media_url"],
                    "permalink": post["permalink"],
                    "timestamp": post["timestamp"],
                },
            )

        db_posts = Post.objects.all()
        posts_del = [post for post in db_posts if post.instagram_id not in instagram_ids]
                   
        for post in posts_del:
            post.delete()

    @staticmethod
    def post_comment_to_instagram(insta_id: str, text: str) -> dict:
        """Create comment"""
        url = f"https://graph.instagram.com/v22.0/{insta_id}/comments"

        data = {
            "access_token": ACCESS_TOKEN,
            "message": text
        }

        response = requests.post(url, data=data)

        if response.status_code != 200:
            raise Exception("Failed to create instagram comment")

        return response.json()

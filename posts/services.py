from config import settings
import requests
from posts.models import *

ACCESS_TOKEN = settings.INSTAGRAM_ACCESS_TOKEN

class SyncService: 
    @staticmethod
    def get_posts():
        url = f"https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,permalink,timestamp&access_token={ACCESS_TOKEN}"
        all_posts = []

        
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            all_posts.extend(data.get("data", []))
            url = data.get("paging", {}).get("next")
                            
        return all_posts
    
    @staticmethod
    def upsert(posts_data):
        for post in posts_data:
            Post.objects.update_or_create(
                instagram_id=post["id"], #using for seearch
                defaults={
                    "media_type": post["media_type"],
                    "media_url": post["media_url"],
                    "permalink": post["permalink"],
                    "timestamp": post["timestamp"],
                    }
            )
 

        

        


from django.contrib import admin
from django.urls import path
from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sync/', SyncPostsView.as_view()),
    path('api/posts/', ListPostsView.as_view()),
    path('api/posts/<int:pk>/comment/', PostCommentsView.as_view())
]

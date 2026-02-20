from django.contrib import admin
from django.urls import path
from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sync/', PostSyncView.as_view()),
    path('api/posts/', PostListView.as_view()),
    path('api/posts/<int:pk>/comment/', PostCommentCreateView.as_view())
]

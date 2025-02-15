from django.urls import path
from .views import (
    PostListView,PostDetailView,PostFileListView,PostFileDetailView,
    CommentListView,CommentDetailView,LikeListView,LikeDetialView
)

urlpatterns = [
    path('post/',PostListView.as_view(),name='post-list'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('file/',PostFileListView.as_view(),name='file-list'),
    path('file/<int:pk>/',PostFileDetailView.as_view(),name='post-detail'),
    path('comment/',CommentListView.as_view(),name='comment-list'),
    path('comment/<int:pk>/',CommentDetailView.as_view(),name="comment-detail"),
    path('like/',LikeListView.as_view(),name='like-list'),
    path('like/<int:pk>/',LikeDetialView.as_view(),name='like-detail')
]
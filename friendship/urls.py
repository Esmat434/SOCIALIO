from django.urls import path
from .views import (
    UserListView,UserDetail,RequstView,RequestListView,AcceptView,FriendListView
    )

urlpatterns = [
    path('user/',UserListView.as_view(),name="user-list"),
    path('user/<str:username>/',UserDetail.as_view(),name='user-detail'),
    path('request/',RequstView.as_view(),name='request'),
    path('request/list/',RequestListView.as_view(),name='request-list'),
    path('request/accept/',AcceptView.as_view(),name='accept'),
    path('friends/',FriendListView.as_view(),name='friend-list')
]
from django.urls import path
from .views import PostList, PostDetail, userPostList, PostUpdate, PostDelete, CreateCommentAPI, CreateLikeAPI, PostCreateApi
urlpatterns = [
    
    path('list/', PostList.as_view()),
    path("postlist/", userPostList.as_view(), name="user-list"),
    path("create/", PostCreateApi.as_view(), name="create"),
    path('<str:slug>/', PostDetail.as_view(), name="detail"),
    path("update/<str:slug>/", PostUpdate.as_view(), name="update"),
    path('delete/<str:slug>/', PostDelete.as_view(), name="delete"),
    path('like/<str:slug>/', CreateLikeAPI.as_view(), name="like"),
    path('comment/<str:slug>/', CreateCommentAPI.as_view(), name="comment"),
    
]

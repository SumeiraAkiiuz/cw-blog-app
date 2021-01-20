from django.urls import path
from .views import CategoryList, CategoryDetail, PostDetail

urlpatterns = [
    path("", CategoryList.as_view(), name="category"),
    path("<category>/", CategoryDetail.as_view(), name="category-detail"),
    path("post/<title>/", PostDetail.as_view(), name="post"),
    # path("", CommentList.as_view(), name="comment"),
    # path("", LikeList.as_view(), name="like"),
    
    
]

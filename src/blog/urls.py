from django.urls import path
from .views import PostList, PostDetail, comment_api
urlpatterns = [
    
    path('', PostList.as_view()),
    # path('<int:pk>/', PostDetail.as_view()),
    path('<str:slug>/', PostDetail.as_view(), name="detail"),
    path('<slug>/comment/', comment_api, name='comment_post'),
   
]

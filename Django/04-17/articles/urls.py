from django.urls import path
from articles import views

# app_name = 
# name = 
# templates에서 url named pattern에 사용하려고

urlpatterns = [
    # 전체 게시글
    path('articles/', views.article_list),
    # 단일 게시글
    path('articles/<int:article_pk>/', views.article_detail),
    # 전체 댓글
    path('comments/', views.comment_list),
    # 단일 댓글
    path('comments/<int:comment_pk>/', views.comment_detail),
]

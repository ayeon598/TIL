from django.urls import path
from articles import views

# app_name / name 사용하는 이유 : templates에서 url named pattern에 사용하려고

urlpatterns = [
    # 전체 게시글
    path('articles/', views.article_list),
    # 단일 게시글
    path('articles/<int:article_pk>/', views.article_detail),
]
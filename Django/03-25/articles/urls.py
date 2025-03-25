from django.contrib import admin
from django.urls import path
# . 은 현재 디렉토리
from . import views

# URL namespace
# 앱이 여러개라면, 다른앱과 혼동하지 않기 위해
app_name = 'articles' # 우리가 만든 앱과 이름이 같을 필요는 없지만 헷갈리지 않도록 보통 같게 함.

# href = "http://127.0.0.1:8000/articles/index/"
# url named pattern
# {% url articlse:index %}
# href 대신 이렇게 쓰기 위해 name을 설정
urlpatterns = [
    path('index/', views.index, name="index"),
    path('dinner/', views.dinner, name="dinner"),
    path('search/', views.search, name="search"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
]
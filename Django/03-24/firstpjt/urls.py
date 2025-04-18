"""
URL configuration for firstpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# articles 안에 있는 views.py
from articles import views

urlpatterns = [
    # 127.0.0.1/8000/admin/ 관리자페이지로 접근
    path('admin/', admin.site.urls),
    # 127.0.0.1/8000/articles/url로 접근하면
    # views.py에 index함수로 접근
    path('articles/', views.index),
]

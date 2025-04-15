from django.urls import path
from . import views

app_name = 'crawlings'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
    path('search/', views.search, name='search'),
]

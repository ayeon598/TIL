from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

# 홈페이지에서 게시글 조회, 게시글 생성
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # DB에 Article 모델의 데이터가 없을 경우 404에러 발생
        articles = get_list_or_404(Article)
        # 직렬화(django data를 json으로 변경)
        # many=True : 객체가 여러개일 때
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        # 유효성 검사
        # 데이터 제출(생성) 성공 시 HTTP_201
        # 데이터 제출(생성) 실패 시 HTTP_400
        # raise_exception=True : 유효성 검사에서 실패했을 때 예외 발생(HTTP_400)
        # => 유효성 검사 실패했을 때의 response를 안 써도 됨.
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효성 검사 실패했을 때
        # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# 단일 게시글 조회, 삭제, 수정
# Restful API : GET, POST, PUT, DELETE
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # get_object_or_404 : 단일 게시물
    article = get_object_or_404(Article, pk=article_pk)
    # 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # 삭제
    if request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 수정
    if request.method == 'PUT':
        # partial = True : 부분 업데이트 허용(일부 필드만 수정 가능)
        serializer = ArticleSerializer(
            article, data = request.data, partial = True
        )
        # raise_exception=True : 유효성 검사에서 실패했을 때 예외 발생(HTTP_400)
        # => 유효성 검사 실패했을 때의 response를 안 써도 됨.
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # 유효성 검사 실패했을 때
        # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
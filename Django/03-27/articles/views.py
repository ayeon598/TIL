from django.shortcuts import render

# 현재 디렉토리의 models.py로부터 Board 모델을 가져오겠다.
from .models import Board

def index(request):
    # QuerySetAPI ---> Read, 전체 데이터 조회 : Board.objects.all()
    articles = Board.objects.all()

    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)
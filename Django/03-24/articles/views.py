from django.shortcuts import render

# Create your views here.
def index(request):
    # 페이지를 렌더링하겠다 == html 페이지를 띄워주겠다. // 리다이렉트로
    # articles 앱의 index.html 페이지를 렌더링 하겠다.
    return render(request, 'articles/index.html')
from django.shortcuts import render, redirect

# Create your views here.

# articles -> model form
# accounts -> built-in form

from django.contrib.auth.forms import (
    AuthenticationForm, # 로그인을 위한 폼 bult-in form
    UserCreationForm, # 회원가입(db 저장.번경) - model form
    PasswordChangeForm, # 비밀번호 변경 bult-in form
)

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .models import User


from django.contrib.auth.decorators import login_required

def login(request):
    # 아이디와 패스워드 입력하고 로그인 버튼(submit)버튼 눌렀을 때
    if request.method == 'POST':
        # request.POST : 아이디, 비밀번호
        # request : user <--- AuthenticationMiddleware
        form = AuthenticationForm(request, request.POST)
        # 유효성 검사
        if form.is_valid():
            # get_user() : 인증된 사용자의 객체
            # signup(회원가입)과 차이 ---> 이미 DB에 존재하는 사용자를 인증
            auth_login(request, form.get_user())
            return redirect('articles:index')
    
    # ---------------------------------------------------------------------------

    # 로그인 버튼(submit) 누르기 전
    else:
        form = AuthenticationForm() # 빈 폼

    # GET요청 or 유효성 검사 실패
    context = {
        'form' : form # 빈 폼
    }
    
    return render(request, 'accounts/login.html', context)

# 로그인을 한 사용자만 로그아웃을 할 수 있다.
@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

from .forms import CustomUserCreationForm, CustomUserChangeForm

def signup(request):
    # 이미 존재하는 회원
    if request.user.is_authenticated:
        return redirect('articles:index')

    # 새로 회원가입(submit 버튼 눌렀을때)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 1. 유효성 검사
            user = form.save() # 2. DB에 저장
            auth_login(request, user) # 3. 로그인
            return redirect('articles:index')
    else: # submit 버튼 누르기 전
        form = CustomUserCreationForm() # 빈폼
    # 유효성검사 실패
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    # request.user : 현재 로그인 되어있는 user
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    # submit버튼 눌렀을 때
    if request.method == 'POST':
        # request.POST : 회원 정보에 입력한 수정사항
        form = CustomUserChangeForm(request.POST, instance = request.user)
        # 유효성검사
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    
    else: # submit 버튼 누르기 전
        form = CustomUserChangeForm(instance = request.user)
    # 유효성검사 실패 or GET 요청
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html', context)

from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request, user_pk):
    # 비밀번호 변경 버튼 눌렀을 떄
    if request.method == 'POST':
        # 왜 request.user 먼저 나올까?
        # 부모클래스인 SetPasswordForm의 생성자 함수 첫번째 인자가 user
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호 변경하고 로그인 유지할지 안할지
            update_session_auth_hash(request, user)
            # 로그인 유지하고 리다이렉트
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user) # 빈폼 X (현재 로그인한 사용자)
    
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)

from django.contrib.auth import get_user_model

# 반드시 로그인한 사용자일 필요는 없음
def profile(request, username):
    User = get_user_model()
    # person : 게시글을 작성한 사용자(로그인한 사용자 X)
    person = User.objects.get(username=username)
    context = {
        'person' : person
    }
    return render(request, 'accounts/profile.html', context)

from django.http import JsonResponse

@login_required
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user

    # 자기자신 팔로우 불가능
    if me != you:
        # 팔로우가 되어있다면 
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed = False # 언팔로우
        else:
            you.followers.add(me)
            is_followed = True # 팔로우

        context = {
            'is_followed' : is_followed,    # True : 팔로우 / False : 언팔로우
            'followings_count' : you.followings.count(), # 팔로잉 수
            'followers_count' : you.followers.count(),  # 팔로워 수
        }

        return JsonResponse(context)
    
    # POST요청이므로 redirect
    return redirect('accounts:profile', you.username)
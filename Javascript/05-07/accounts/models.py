from django.db import models

# Create your models here.

# AbstractUser : 자동으로 필드를 제공(로그인, 권한 관리 등)
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # symmetrical=False (대칭이 False)
    # : 내가 카리나를 팔로잉 했다고, 카리나가 나를 팔로우 한건 아니다.
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers'
    )
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # class Meta : 폼의 기본 구조를 자동으로 생성
    # 위젯으로 세부 조정 가능
    class Meta:
        model = Article
        # fields = ('title', 'content', 'created_at', 'updated_at')
        fields = '__all__'
        # 한두개 정도 필드를 제외하고 싶다: exclude
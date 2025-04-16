from rest_framework import serializers
from .models import Article

# serializers : 직렬화
# django data를 json로 바꿔준다.

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
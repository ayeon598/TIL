from django.db import models

# Create your models here.
class Comment(models.Model):
    company = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.company}({self.code})] {self.content[:30]}"
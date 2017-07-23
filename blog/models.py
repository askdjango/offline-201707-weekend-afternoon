from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, help_text='이름 3글자만 넣어주세요.')
    content = models.TextField(help_text='Markdown 문법을 지원합니다.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


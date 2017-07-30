from django.conf import settings
from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


def min_length_3_validator(value):
    if len(value) < 3:
        raise ValidationError('3글자 이상 입력해주세요.')


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    # author = models.CharField(max_length=20)
    title = models.CharField(max_length=100,
            validators=[min_length_3_validator],
            help_text='이름 3글자만 넣어주세요.')
    photo = models.ImageField(upload_to='blog/post/%Y/%m/%d')
    content = models.TextField(help_text='Markdown 문법을 지원합니다.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return '/weblog/{}/'.format(self.id)
        return reverse('blog:post_detail', args=[self.id])


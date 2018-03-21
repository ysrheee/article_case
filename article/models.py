from django.db import models
from user.models import Profile


# Create your models here.

class Article(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    _RATING = (
        (ONE, '1점'),
        (TWO, '2점'),
        (THREE, '3점'),
        (FOUR, '4점'),
        (FIVE, '5점')
    )

    name = models.CharField(max_length=120, verbose_name='글 제목')
    link = models.URLField(verbose_name='글 링크')
    summary = models.TextField(blank=True, null=True, verbose_name='글 요약')
    will_summary = models.BooleanField(verbose_name='글 요약할 것인지')
    rate = models.IntegerField(choices=_RATING, verbose_name='점수')
    enable = models.BooleanField(default=True, verbose_name='삭제 여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 시점')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정 시점')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '글 및 글 요약'
        verbose_name_plural = '글 및 글 요약'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=120, verbose_name='태그 이름')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='태그 생성 시점')

    class Meta:
        verbose_name = '태그'
        verbose_name_plural = '태그'

    def __str__(self):
        return self.name


class ArticleHasTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '테이블 연결: Article, Tag'
        verbose_name_plural = '테이블 연결: Article, Tag'
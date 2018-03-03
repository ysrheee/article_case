# coding: utf-8


from django.urls import include, path
from article.api.web import get_articles, create_article, create_tag


urlpatterns = [
    path('', get_articles),
    path('create/', create_article),
    path('tag/create/', create_tag)
]
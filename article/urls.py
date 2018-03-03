# coding: utf-8


from django.urls import include, path
from article.api.web import articles, create_article


urlpatterns = [
    path('', articles),
    path('create', create_article)
]
# coding: utf-8


from django.urls import path

from article.api.web import *

urlpatterns = [
    path('', articles_get),
    path('create', article_create),
    path('tag/create', tag_create),
    path('tag/get', all_tags_used_get)
]
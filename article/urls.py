# coding: utf-8


from django.urls import include, path
from article.api.web import *


urlpatterns = [
    path('', articles_get),
    path('create/', article_create),
    path('tag/create/', tag_create)
]
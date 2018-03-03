# coding: utf-8


from django.urls import include, path
from article.api.web import signup


urlpatterns = [
    path('signup/', signup),
]
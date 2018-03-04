import json

from django.core import serializers
from django.http.request import HttpRequest
from typing import Dict, List
from article.models import Article, ArticleHasTag


def article_request_to_dic(request: HttpRequest) -> Dict:
    params = {}
    keys = ['name', 'link', 'summary', 'will_summary', 'rate', 'profile']
    for key in keys:
        item = request.POST.get(key)
        if item:
            params[key] = item
    return params


def tag_request_to_dic(request: HttpRequest) -> Dict:
    params = {}
    keys = ['name']
    for key in keys:
        item = request.POST.get(key)
        if item:
            params[key] = item
    return params


def article_object_to_dic(article: Article):
    return {
        'id': article.id,
        'name': article.name,
        'link': article.link,
        'summary': article.summary,
        'will_summary': article.will_summary,
        'rate': article.rate,
        'created_at': article.created_at,
        'updated_at': article.updated_at
    }


def article_object_to_dic(article: Article):
    tags = ArticleHasTag.objects.filter(
        article=article
    ).values_list('tag__name', flat=True)

    return {
        'id': article.id,
        'name': article.name,
        'link': article.link,
        'summary': article.summary,
        'will_summary': article.will_summary,
        'rate': article.rate,
        'created_at': article.created_at,
        'updated_at': article.updated_at,
        'tags': list(tags)
    }

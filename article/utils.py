from django.http.request import HttpRequest
from typing import Dict, List
from article.models import Article


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


def article_object_to_dic(articles: Article):
    return {
        'id': articles.id,
        'name': articles.name,
        'link': articles.link,
        'summary': articles.summary,
        'will_summary': articles.will_summary,
        'rate': articles.rate,
        'created_at': articles.created_at,
        'updated_at': articles.updated_at
    }


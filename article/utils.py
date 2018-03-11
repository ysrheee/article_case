from typing import Dict

from django.http.request import HttpRequest

from article.models import Article, ArticleHasTag, Tag


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


def tag_object_from_article(article: Article):
    tags = ArticleHasTag.objects.filter(
        article=article
    ).values_list('tag__name', flat=True)

    return list(tags)


def append_all_lists(lists):
    fin_list = []
    for li in lists:
        for l in li:
            fin_list.append(l)
    return fin_list

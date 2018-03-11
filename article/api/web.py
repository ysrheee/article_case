# coding: utf-8


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from article.helper import *


@csrf_exempt
# @require_http_methods(["POST"])
def articles_get(request):
    try:
        articles = get_articles_to_map_list(request)
        print(articles)
        return JsonResponse(articles, safe=False)
    except Exception as e:
        print(e)
        data = {'result': 'fail'}
        return JsonResponse(data)


@csrf_exempt
# @require_http_methods(["POST"])
def article_create(request):
    data = {'result': 'success'}
    try:
        create_article(request)
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data['result'] = 'fail'
        return JsonResponse(data)


@csrf_exempt
# @require_http_methods(["POST"])
def all_tags_used_get(request):
    try:
        tags = get_all_tags(request)
        return JsonResponse(tags, safe=False)
    except Exception as e:
        print(e)
        data = {'result': 'fail'}
        return JsonResponse(data)


def tags_in_article_get(request):
    try:
        tags = get_tags_in_article(request)
        return JsonResponse(tags, safe=False)
    except Exception as e:
        print(e)
        data = {'result': 'fail'}
        return JsonResponse(data)


@csrf_exempt
# @require_http_methods(["POST"])
def tag_create(request):
    data = {'result': 'success'}
    try:
        create_tag(request)
        return JsonResponse(data)
    except:
        data['result'] = 'fail'
        return JsonResponse(data)

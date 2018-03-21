# coding: utf-8


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from article.helper import *

"""
input: user info
return: article list of the user
"""


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


"""
input: article, tags info
return: success or fail
"""


@csrf_exempt
# @require_http_methods(["POST"])
def article_create(request):
    request = body_to_querydict(request)
    data = {'result': 'success'}
    try:
        create_article(request)
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data['result'] = 'fail'
        return JsonResponse(data)


"""
input: user info
return: all tag list used by the user
"""


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


"""
input: article info
return: all tag list in the article
"""


def tags_in_article_get(request):
    try:
        tags = get_tags_in_article(request)
        return JsonResponse(tags, safe=False)
    except Exception as e:
        print(e)
        data = {'result': 'fail'}
        return JsonResponse(data)


"""
input: tag info
return: success or fail
"""


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

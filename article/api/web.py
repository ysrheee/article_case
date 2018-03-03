# coding: utf-8


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from article.helper import get_articles, create_article, create_tag


@csrf_exempt
# @require_http_methods(["POST"])
def articles_get(request):
    try:
        articles = get_articles(request)
        return JsonResponse(articles, safe=False)
    except Exception as e:
        print(e)
        data = {'result': 'fail'}
        return JsonResponse(data)


def article_create(request):
    data = {'result': 'success'}
    try:
        create_article(request)
        return JsonResponse(data)
    except:
        data['result'] = 'fail'
        return JsonResponse(data)


def tag_create(request):
    data = {'result': 'success'}
    try:
        create_tag(request)
        return JsonResponse(data)
    except:
        data['result'] = 'fail'
        return JsonResponse(data)

# coding: utf-8


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from article.helper import get_articles_to_map_list, create_article, create_tag


@csrf_exempt
# @require_http_methods(["POST"])
def articles_get(request):
    try:
        articles = get_articles_to_map_list(request)
        return JsonResponse(articles, safe=False)
    except Exception as e:
        print(e)
        data = {'result': 'fail'}
        return JsonResponse(data)


#TODO: List(Article-Tags) 불러오는 메소드 구현해야 함
@csrf_exempt
# @require_http_methods(["POST"])
def articles_with_tags_get(request):
    try:
        tags =
        return JsonResponse(tags, safe=False)
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
    except:
        data['result'] = 'fail'
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

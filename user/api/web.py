# coding: utf-8


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from article.utils import body_to_querydict
from user.helper import *


@csrf_exempt
# @require_http_methods(["POST"])
def signup(request):
    request = body_to_querydict(request)
    data = {'result': 'fail'}
    try:
        sign_up(request)
        log_in(request)
        data['result'] = 'success'
        return JsonResponse(data)
    except Exception as e:
        print(e)
        return JsonResponse(data)

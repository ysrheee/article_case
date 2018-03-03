# coding: utf-8


from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_exempt
#@require_http_methods(["POST"])
def signup(request):
    data = {'result': 'fail'}
    

    data['result'] = 'success'
    return JsonResponse(data)
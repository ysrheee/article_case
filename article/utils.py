from django.http.request import HttpRequest
from typing import Dict, List


def article_request_to_dic(request: HttpRequest) -> Dict:
    params = {}
    keys = ['name', 'link', 'summary', 'will_summary', 'rate', 'user_id']
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

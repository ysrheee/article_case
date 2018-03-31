from typing import Dict

from django.http import HttpRequest


def signup_request_to_dic(request: HttpRequest) -> Dict:
    params = {}
    keys = ['email', 'password']

    for key in keys:
        item = request.POST.get(key)
        if item:
            params[key] = item

    return params

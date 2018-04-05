from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from user.models import *
from article.utils import body_to_querydict
from user.utils import password_to_md5


@csrf_exempt
@require_http_methods(["POST"])
def sign_up(request: HttpRequest):
    data = {}
    try:
        request = body_to_querydict(request)

        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            pass
        user = User(username=email)
        user.email = email
        user.set_password(password)
        user.save()

        profile = Profile(user=user)
        profile.save()

        new_user = authenticate(request, username=email, password=password)

        auth_login(request, new_user)

        data['result'] = 'success'
        return JsonResponse(data)

    except Exception as e:
        print(e)
        data['result'] = 'fail'
        return JsonResponse(data)


@csrf_exempt
@require_http_methods(["POST"])
def log_in(request: HttpRequest):
    data = {}

    try:
        request = body_to_querydict(request)

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        auth_login(request, user)

        data['result'] = 'success'
        return JsonResponse(data)

    except Exception as e:
        print(e)
        data['result'] = 'fail'
        return JsonResponse(data)


def log_out(request: HttpRequest):
    auth_logout(request)
    return redirect('/')

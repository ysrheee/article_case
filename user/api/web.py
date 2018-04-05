from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from user.models import *
from article.utils import body_to_querydict


@csrf_exempt
@require_http_methods(["POST"])
def sign_up(request: HttpRequest):
    data = {}
    try:
        request = body_to_querydict(request)

        email = request.POST.get('email')
        password_raw = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            pass
        user = User(username=email)
        user.email = email
        user.set_password(password_raw)
        user.save()

        profile = Profile(user=user)
        profile.save()

        new_user = authenticate(username=user.username, password=user.password)

        auth_login(request, new_user)

        data['result'] = 'success'
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data['result'] = 'fail'
        return JsonResponse(data)


def log_in(request: HttpRequest):
    data = {}
    request = body_to_querydict(request)

    email = request.POST.get('email')
    password_raw = request.POST.get('password')

    new_user = authenticate(email=email, password=password_raw)

    user = User(username=email)
    auth_login(request, user)


def log_out(request: HttpRequest):
    print("A")

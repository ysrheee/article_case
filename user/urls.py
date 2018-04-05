# coding: utf-8


from django.urls import include, path
from user.api.web import sign_up, log_in, log_out

urlpatterns = [
    path('signup/', sign_up),
    path('login/', log_in),
    path('logout', log_out)
]
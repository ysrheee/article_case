# coding: utf-8


from django.urls import include, path
from user.api.web import signup


urlpatterns = [
    path('signup/', signup),
]
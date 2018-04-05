# !/usr/bin/python
# -*- coding: utf-8

from django import template

register = template.Library()


@register.filter(name='get_profile')
def get_profile(request, key):
    email = ""

    if request.user.is_authenticated:
        email = request.user

    data = {
        "email": email
        }


    return data[key]


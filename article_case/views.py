# coding: utf-8

from django.shortcuts import render



def rendering_to_articlebox(request):
    return render(request, 'article_box.html')


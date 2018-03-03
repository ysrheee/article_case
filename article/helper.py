# DB Access 하는 Method
from article.models import Article, Tag
from article.utils import *


def get_articles(request: HttpRequest):
    articles = Article.objects.filter(
        user_id=request.POST.get('user_id'),
        enable=True
    ).order_by('-created_at')
    return list(map(article_object_to_dic, articles))


def create_article(request: HttpRequest):
    params = article_request_to_dic(request)
    article = Article.objects.create(
        name=params.get('name'),
        link=params.get('link'),
        summary=params.get('summary'),
        will_summary=params.get('will_summary'),
        rate=params.get('rate'),
        user_id=params.get('user_id')
    )
    article.save()


def create_tag(request: HttpRequest):
    params = tag_request_to_dic(request)
    tag = Tag.objects.create(
        name=params.get('name')
    )
    tag.save()


"""
def get_articles():

def get_tags():
"""

# DB Access 하는 Method
from article.models import Article, Tag
from article.utils import *


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

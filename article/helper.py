# DB Access 하는 Method
from article.models import *
from article.utils import *
from user.models import Profile


def get_articles(request: HttpRequest):
    user = request.user
    profile = Profile.objects.get(user=user)
    if not profile:
        return False
    articles = Article.objects.filter(
        profile=profile,
        enable=True
    ).order_by('-created_at')
    return articles


def get_articles_to_map_list(request: HttpRequest):
    articles = get_articles(request)
    return list(map(article_object_to_dic, articles))


def get_all_tags(request: HttpRequest):
    articles = get_articles(request)
    tag_lists = map(tag_object_from_article, articles)
    return append_all_lists(tag_lists)


def create_article(request: HttpRequest):
    params = article_request_to_dic(request)
    article = Article.objects.create(
        name=params.get('name'),
        link=params.get('link'),
        summary=params.get('summary'),
        will_summary=params.get('will_summary'),
        rate=params.get('rate'),
        profile=params.get('profile')
    )
    article.save()


def create_tag(request: HttpRequest):
    params = tag_request_to_dic(request)
    tag = Tag.objects.create(
        name=params.get('name')
    )
    tag.save()

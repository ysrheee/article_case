# DB Access 하는 Method
from article.utils import *
from user.models import Profile


# TODO: Client에서 Article Id를 어떻게 받아오는지를 알아야 함.
def get_article(request: HttpRequest):
    return Article.object.get(id=request.id)


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


def get_tags_in_article(request: HttpRequest):
    article = get_articles(request)
    tags = ArticleHasTag.objects.filter(
        article=article
    ).values_list('tag__name', flat=True)
    return tags


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

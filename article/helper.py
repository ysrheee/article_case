# DB Access 하는 Method
from article.utils import *
from user.models import Profile


# TODO: Client에서 Article Id를 어떻게 받아오는지를 알아야 함.
# Works
def get_article(request: HttpRequest):
    return Article.objects.get(id=request.id)
    # return Article.objects.get(id=1)


# Works
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


# Works
def get_articles_to_map_list(request: HttpRequest):
    articles = get_articles(request)
    return list(map(article_object_to_dic, articles))


# Works?
def get_tags_in_article(request: HttpRequest):
    article = get_article(request)
    tags = ArticleHasTag.objects.filter(
        article=article
    ).values_list('tag__name', flat=True)
    return list(tags)


def get_all_tags(request: HttpRequest):
    articles = get_articles(request)
    tag_lists = map(tag_object_from_article, articles)
    return append_all_lists(tag_lists)


# Works
# TODO: params['tags'] = ['창조과학', '창업'] 넣어서 tag랑 같이 저장되는지 테스트
def create_article(request: HttpRequest):
    profile = Profile.objects.get(user=request.user)
    params = article_request_to_dic(request)
    article = Article.objects.create(
        name=params.get('name'),
        link=params.get('link'),
        summary=params.get('summary'),
        will_summary=params.get('will_summary'),
        rate=params.get('rate'),
        profile=profile
    )
    article.save()
    tags = params.get('tags')
    for tag in tags:
        tag_new = Tag.object.get_or_create(
            name=tag
        )
        tag_new.save()
        article_has_tag = ArticleHasTag.object.create(
            article=article, tag=tag_new
        )
        article_has_tag.save()


# Works
def create_tag(request: HttpRequest):
    params = tag_request_to_dic(request)
    tag, created = Tag.objects.get_or_create(
        name=params.get('name')
    )
    tag.save()


#
def count_article(request: HttpRequest):
    articles = get_articles(request)
    return len(articles)
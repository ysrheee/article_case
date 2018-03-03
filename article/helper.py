# DB Access 하는 Method
from article.models import Tag, Article, ArticleHasTag
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


#TODO: List(Article-Tags) 불러오는 메소드 구현해야 함
def get_articles_with_tags(request: HttpRequest):
    articles = get_articles(request)
    articles_with_tags = ArticleHasTag.objects.filter(
        article=articles
    )



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


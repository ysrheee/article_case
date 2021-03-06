from django.contrib import admin
from article.models import *


# Register your models here.
class ArticleHasTagInline(admin.TabularInline):
    model = ArticleHasTag


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleHasTagInline
    ]

    list_display = ('id', 'name', 'link', 'summary', 'will_summary', 'rate', 'profile')


admin.site.register(Article, ArticleAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Tag, TagAdmin)


class ArticleHasTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'article')


admin.site.register(ArticleHasTag, ArticleHasTagAdmin)
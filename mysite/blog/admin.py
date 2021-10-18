from django.contrib import admin
from .models import Article, ArticleComment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'date')


class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'commentator_name', 'commentator_email', 'date_created', 'content')


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleComment, ArticleCommentAdmin)

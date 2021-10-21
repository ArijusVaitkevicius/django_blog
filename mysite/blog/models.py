from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField('Title', max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField('Date', auto_now_add=True)
    text = HTMLField()

    def __str__(self):
        return f'{self.title} ({self.author})'

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    @property
    def comments_total(self):
        all_comments = ArticleComment.objects.filter(article=self.id)
        return len(all_comments)


class ArticleComment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    commentator_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    commentator_email = models.CharField('Email', max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Comment', max_length=2000)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

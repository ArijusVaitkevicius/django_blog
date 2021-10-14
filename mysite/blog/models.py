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

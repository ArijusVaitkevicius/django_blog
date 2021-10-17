from django.views import generic
from .models import Article
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'index.html')


class ArticlesListView(generic.ListView):
    model = Article
    template_name = 'articles.html'
    paginate_by = 2

    def get_queryset(self):
        return Article.objects.order_by('-date')


def article(request, article_id):
    single_article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article.html', {'article': single_article})

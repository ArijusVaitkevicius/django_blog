from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Article


def index(request):
    return render(request, 'index.html')


class ArticlesListView(generic.ListView):
    model = Article
    template_name = 'articles.html'
    paginate_by = 1

    def get_queryset(self):
        return Article.objects.order_by('-date')

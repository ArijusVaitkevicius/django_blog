from .models import Article
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.forms import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


class NewArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    fields = ['title', 'text']
    success_url = "/blog/articles/"
    template_name = 'article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Article
    fields = ['title', 'text']
    success_url = "/blog/articles/"
    template_name = 'article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cur_article = self.get_object()
        return self.request.user == cur_article.author


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Article
    success_url = "/blog/articles/"
    template_name = 'article_delete.html'

    def test_func(self):
        cur_article = self.get_object()
        return self.request.user == cur_article.author


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} is already in use!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Email {email} is already in use!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    return render(request, 'register.html')
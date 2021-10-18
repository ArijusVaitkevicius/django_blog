from django.views import generic
from .models import Article
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


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
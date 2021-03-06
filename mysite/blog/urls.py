from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.ArticlesListView.as_view(), name='articles'),
    path('articles/<int:article_id>', views.article, name='article'),
    path('articles/new', views.NewArticleCreateView.as_view(), name='new-article'),
    path('articles/<int:pk>/update', views.ArticleUpdateView.as_view(), name='article-update'),
    path('articles/<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]

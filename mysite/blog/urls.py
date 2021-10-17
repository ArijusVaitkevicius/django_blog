from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.ArticlesListView.as_view(), name='articles'),
    path('articles/<int:article_id>', views.article, name='article'),
]
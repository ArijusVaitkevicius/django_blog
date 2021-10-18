from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.ArticlesListView.as_view(), name='articles'),
    path('articles/<int:article_id>', views.article, name='article'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]

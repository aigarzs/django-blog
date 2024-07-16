from django.urls import path
from hexlet_django_blog.articles import views
from hexlet_django_blog.articles.views import (ArticleIndexView, ArticleView,
                                               ArticleCommentCreateView,
                                               ArticleCreateView,
                                               ArticleEditView,
                                               ArticleDeleteView)

urlpatterns = [
    path('', ArticleIndexView.as_view(), name="articles"),
    path("<int:id>/edit/", ArticleEditView.as_view(), name="article_edit"),
    path("<int:id>/delete/", ArticleDeleteView.as_view(),
         name="article_delete"),
    path("<int:id>/", ArticleView.as_view(), name="article"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("<int:id>/comments/", ArticleCommentCreateView.as_view(),
         name="comment_create")
]

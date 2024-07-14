from django.urls import path
from hexlet_django_blog.articles import views
from hexlet_django_blog.articles.views import ArticleIndexView, ArticleView, \
    ArticleCommentCreateView

urlpatterns = [
    path('', ArticleIndexView.as_view()),
    path("<int:id>", ArticleView.as_view(), name="article"),
    path("<int:id>/comments/", ArticleCommentCreateView.as_view(),
         name="comment_create")
]

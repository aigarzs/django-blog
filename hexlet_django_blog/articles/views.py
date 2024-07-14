from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.articles.models import Article, ArticleComment
from .forms import ArticleCommentForm, ArticleForm


# Create your views here.


class ArticleIndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        context = {'appname': 'Simple Django Blog', 'articles': articles}
        return render(request, "articles/index.html", context=context)


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        comments = ArticleComment.objects.filter(article_id=article.id)
        return render(request, "articles/show.html",
                      context={"article": article, "comments": comments})


class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html",
                      context={"form": form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')

        return render(request, 'articles/create.html', {'form': form})


class ArticleCommentCreateView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs["id"]
        form = ArticleCommentForm(
            initial={'article_id': article_id})  # Создаем экземпляр нашей формы
        return render(request, 'articles/comment.html',
                      {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(
            request.POST)  # Получаем данные формы из запроса
        article_id = kwargs["id"]
        if form.is_valid():  # Проверяем данные формы на корректность
            form.save()  # Сохраняем форму
            return redirect("article", id=article_id)
        else:
            return redirect("comment_create", id=article_id)

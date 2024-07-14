from django.db import models


# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ArticleComment(models.Model):
    author = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

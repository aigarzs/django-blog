import django.forms as forms
from .models import ArticleComment


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["author", "content", "article_id"]
        widgets = {"article_id": forms.HiddenInput(), "content": forms.Textarea()}
        labels = {"author": "autors", "content": "komentārs"}


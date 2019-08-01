from django import forms
from articles.models import Article
from markdownx.fields import MarkdownxFormField


class ArticleForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())  # 隐藏
    edited = forms.BooleanField(widget=forms.HiddenInput(), required=False, initial=False)  # 隐藏
    content = MarkdownxFormField()

    class Meta:
        model = Article
        fields = ["title", "content", "image", "tags"]

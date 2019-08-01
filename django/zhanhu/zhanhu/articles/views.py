from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView

from articles.models import Article
from articles.forms import ArticleForm


class ArticlesListView(LoginRequiredMixin, ListView):
    """已发布的文章列表"""
    model = Article
    paginate_by = 10
    context_object_name = "articles"
    template_name = 'articles/article_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['popular_tags'] = Article.objects.get_counted_tags()
        return context

    def get_queryset(self):
        return Article.objects.get_published()


class DraftListView(ArticlesListView):
    """草稿箱文章列表"""

    def get_queryset(self):
        """当前的用户的草稿"""
        return Article.objects.filter(user=self.request.user).get_drafts()


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """发表文章"""
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_create.html'
    messages = '您的文章已创建成功'

    # 重写form_valid用于验证用户
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # 文章跳转页面
    def get_success_url(self):
        messages.success(self.request, self.messages)
        return reverse_lazy('articles:list')

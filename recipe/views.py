# 汎用ビューの読み込み
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# モデルの読み込み
from .models import Recipe
from comment.forms import CommentForm

from django.urls import reverse, reverse_lazy
from django import forms


# 自作クラスを定義、ビューを継承
# 一覧表示用のview
class RecipeListView(ListView):
    # 自作クラスにモデルを設定
    model = Recipe

    def get_queryset(self):
        qs = Recipe.objects.all()
        keyword = self.request.GET.get("q")

        if keyword:
            qs = qs.filter(title__contains=keyword)
        return qs


# レシピ作成用のview
class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description", "image"]
    success_url = reverse_lazy("recipe:index")


# 詳細表示用のview
class RecipeDetailView(DetailView):
    # recipe = Recipe.objects.get(id=pk)
    model = Recipe
    """ def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['CommentForm'] = CommentForm()

        return context """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object = self.get_object()
        # self.object = Recipe.objects.get(id=pk)
        context['CommentForm'] = CommentForm(initial={'recipe': self.object})

        return context


# レシピ更新用のview
class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ["title", "content", "description", "image"]

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("recipe:detail", kwargs={"pk": pk})


# レシピ削除用のview
class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipe:index")

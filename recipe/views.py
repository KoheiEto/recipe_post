# 汎用ビューの読み込み
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# モデルの読み込み
from .models import Recipe


# 自作クラスを定義、ビューを継承
# 一覧表示用のview
class RecipeListView(ListView):
    # 自作クラスにモデルを設定
    model = Recipe


# レシピ作成用のview
class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"


# 詳細表示用のview
class RecipeDetailView(DetailView):
    model = Recipe


# レシピ更新用のview
class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"

# レシピ削除用のview
class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = "/"
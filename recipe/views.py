# 汎用ビューの読み込み
from django.views.generic import ListView
# モデルの読み込み
from .models import Recipe

# 自作クラスを定義、ビューを継承
class RecipeListView(ListView):
  # 自作クラスにモデルを設定
  model = Recipe
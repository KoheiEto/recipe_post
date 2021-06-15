from recipe.models import Recipe
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView


class StaffroomTemplateView(TemplateView):
    template_name = "staffroom/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ユーザのログイン可否によりdbからのデータ取得を分ける
        if self.request.user.is_authenticated:
            # 特定されたユーザで絞り込み
            context['recipe_list'] = Recipe.objects.filter(
                user=self.request.user)
        else:
            context['recipe_list'] = None
        return context
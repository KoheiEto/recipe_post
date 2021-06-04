from django.views.generic import TemplateView

from recipe.models import Recipe

class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['recipe_top'] = Recipe.objects.order_by('?')[0]
        context['recipe_list'] = Recipe.objects.order_by("-created")
        
        return context

    def get_queryset(self):
        qs = Recipe.objects.all()
        keyword = self.request.GET.get("q")

        if keyword:
           qs = qs.filter(title__contains=keyword)
        return qs
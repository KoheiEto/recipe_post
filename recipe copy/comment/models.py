from django.db import models

from recipe.models import Recipe

# Create your models here.
class Comment (models.Model):
    # コメント内容
    content = models.TextField()
    # コメント作成日時
    created = models.DateField(auto_now_add=True)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=None, null=True)
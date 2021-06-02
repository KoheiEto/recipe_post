from enum import auto
from django.db import models
from django.views.generic.edit import UpdateView


# Create your models here.
class Recipe(models.Model):
    # タイトル
    title = models.CharField(max_length=200)
    # 内容
    content = models.TextField()
    # 特徴
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to="images/uploaded/", default=None, null=True, blank=True)
    # 作成日
    created = models.DateTimeField(auto_now_add=True)
    # 最終更新日
    modified = models.DateTimeField(auto_now=True)


# データベースにデータ反映する＝マイグレーション
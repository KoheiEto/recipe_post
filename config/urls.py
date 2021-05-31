"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lib.views import IndexTemplateView
from recipe.views import (RecipeListView, RecipeCreateView, RecipeDetailView,
                          RecipeUpdateView, RecipeDeleteView)

urlpatterns = [
    # 管理者ページ
    path('admin/', admin.site.urls),
    # レシピ一覧画面
    path('recipe/', RecipeListView.as_view(), name="recipe-index"),
    # レシピ作成画面
    path('recipe/create', RecipeCreateView.as_view(), name="recipe-create"),
    # レシピ詳細画面
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe-detail"),
    # レシピ更新画面
    path('recipe/<int:pk>/update',
         RecipeUpdateView.as_view(),
         name="recipe-update"),
    # レシピ削除画面
    path('recipe/<int:pk>/delete',
         RecipeDeleteView.as_view(), name="recipe-delete"),
    path('', IndexTemplateView.as_view(), name="index"),
]

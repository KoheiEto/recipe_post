from django.shortcuts import redirect, render
from django.contrib import messages
from comment.forms import CommentForm

# Create your views here.


# コメントを取得して保存
def comment_create(request):
    recipe_id = request.POST.get("recipe")
    content = request.POST.get("content")

    data = {"content": content, "recipe": recipe_id}

    form = CommentForm(data=data)

    if form.is_valid():
        form.save()
        messages.success(request, "コメントを投稿しました。")
    else:
        messages.error(request, "コメントが投稿できませんでした")

    return redirect("recipe:detail", pk=recipe_id)
# Recipe Post

Django で作成したレシピ管理の最小構成プロジェクトです。

## 概要

- レシピのタイトルと内容を保存できる
- SQLite を使ってローカル開発用のデータベースを利用する
- Django 管理画面でデータを確認・管理できる
- まだベース実装の段階で、画面や機能は最小限

## 構成

```text
recipe_post/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── recipe/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── migrations/
├── manage.py
├── db.sqlite3
├── Pipfile
├── Pipfile.lock
└── README.md
```

## セットアップ

### 1. 依存関係をインストール

```bash
cd recipe_post
pipenv install
```

### 2. マイグレーションを実行

```bash
pipenv run python manage.py migrate
```

### 3. 開発サーバーを起動

```bash
pipenv run python manage.py runserver 0.0.0.0:8000
```

### 4. 管理画面を開く

```text
http://localhost:8000/admin/
```

必要なら、管理者アカウントを作成します。

```bash
pipenv run python manage.py createsuperuser
```

## 使い方

### 管理画面から操作

- 管理画面にログイン
- `Recipe` モデルを確認
- レシピを追加・編集・削除

### Python シェルで作成

```bash
pipenv run python manage.py shell
```

```python
from recipe.models import Recipe

Recipe.objects.create(
    title='カレー',
    content='玉ねぎ、にんじん、肉を炒めてルーでとろみをつける。'
)
```

## 補足

- 現在の `config/urls.py` は管理画面用のルートが中心です
- `Recipe` モデルは `title`, `content`, `created`, `modified` を持っています

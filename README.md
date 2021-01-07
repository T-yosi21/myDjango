# アプリ名
myDjango(投稿サイト)
（＊JavaScriptを用いてのニュースアプリを開発したので是非そちらも！）
# 概要
  ログイン機能と、今回は物を販売する想定で商品の情報を投稿できるようにしました

# 本番環境
  URL//
  ログイン情報（テスト用）
  ・ユーザー名：testA
  ・パスワード：test01234

# 作成背景 
現在、web系の開発言語を中心に学習を行なっています。その中でPython言語で
web系フレームワークDjangoに興味を持ちこれを用いて実装していこうと考えました。
今回はシンプルに記事見たい物を投稿しそれを閲覧、編集、削除と言った機能を持たせ
ログイン機能ではバリデーションを細かく実装し、より現実に近い仕様にしております。


# 工夫したポイント
・バックエンド側の実装でクラスベースとファンクションベースの使い分け。
特にフロントでの表示にどのメソットや処理を加えてるかに迷った。
・フロントでは実装の際に記述を減らすべくDB側でオプションの設定で
表示されるようにした

## ログイン画面

# 使用技術
## バックエンド
  Python3.9 Django3.1.4
## フロントエンド
  HTML、CSS, JavaScript
## データベース
  SQlite3
## ソース管理
  GitHub、GitHubDesktop
## エディタ
  VSCode
# DB設計

## Productテーブル
|Column|Type|Options|
|-------|-----|-------|
|title|CharField|max_length=100, verbose_name="タイトル"|
|Price|IntegerField|verbose_name="値段"|
|Explanation|TextField|max_length=200, verbose_name="商品説明"|
|Image|ImageField|upload_to='images', blank=True, null=True|
|pub_date|DateTimeField|auto_now_add=True|
|created_by|CurrentUserField|verbose_name='作成者'|

## Commentテーブル
|Column|Type|Options|
|-------|-----|-------|
|post|ForeignKey|'Product', on_delete=models.CASCADE,verbose_name="記事"|
|author|ForeignKey|'auth.User', on_delete=models.CASCADE, verbose_name="ログイン名"|
|text|TextField|verbose_name="投稿内容"|
|created_date|DateTimeField|auto_now_add=True|
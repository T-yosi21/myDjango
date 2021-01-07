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

## 登録画面
ログイン画面です。今回はユーザ名、パスワードの二つだけで作成できるようにしました。
バリデーション関係はユーザー名が既に登録されている時、パスワードが確認と不一致の時または５文字以上などのを
設定しました。横にあるラベルはフォームクラスを設定しバリデーション、ラベル等の画面に表示する情報を設定し、フロント側での
コード記述を少なくする工夫を行いました。
https://user-images.githubusercontent.com/67937180/103842281-e8926b80-50d8-11eb-94e5-3eeaf05328cd.png

## ログイン画面
こちらも登録画面で入力した2点の情報を入力すればログインできる状態です。バリデーションはジャンゴ側が
用意しているテンプレートを使ってバリデーション、入力フォームを作成しています。
https://user-images.githubusercontent.com/67937180/103842387-2abbad00-50d9-11eb-94a1-46daae39f3e1.png

## メイン画面
投稿した内容を見れる一覧ページです。今回は記事というか主に商品を販売したりするECサイトを
目的として作成したのですが、趣旨が色々変わってしまい不思議なアプリができてしまいました。
ここでは、その変わってしまった記事などをご覧いただけます。。
https://user-images.githubusercontent.com/67937180/103842476-5dfe3c00-50d9-11eb-97d6-6b1beee08661.png

## 新規投稿画面
投稿画面です。3点の入力フォームと1つの選択フォームがあります。
値段以外はテキスト、文字で入力できるのですが値段だけは文字では打てません！そしてなんと
この値段には１円以上で入力しないとエラーになってしまいます。タダではダメです。カテゴリーはこちらで
用意した項目を選択し投稿できます。今後はこの選択できる項目をユーザー自身でカスタマイズできる機能を実装予定です
https://user-images.githubusercontent.com/67937180/103842539-825a1880-50d9-11eb-8e31-e83c72c20a2a.png

## 詳細画面
このページは文字通り投稿した内容を確認できるページになります。ただの確認ページだと面白くないと思い
ここでこの投稿に関してコメントできる機能をつけてみました。コメントはできるのですが、写真があったら会話が盛り上がると思うので
今後はここに画像も一緒に投稿できる機能をつけたいと考えています。
https://user-images.githubusercontent.com/67937180/103842813-04e2d800-50da-11eb-8557-b0303cde9b3b.png
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
from django.db import models
import datetime
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="タイトル")
    Price = models.IntegerField(verbose_name="値段")
    Explanation = models.TextField(max_length=200, verbose_name="商品説明")
    Image = models.ImageField(upload_to='images', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    CHOICES = (
        ('朝飯', '朝飯'),
        ('おかず', 'おかず'),
        ('主食', '主食'),
        ('おつまみ', 'おつまみ'),
        ('その他', 'その他'),
    )
    Choices = models.CharField(
        max_length=10, choices=CHOICES, verbose_name="カテゴリー")

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    post = models.ForeignKey('Product', on_delete=models.CASCADE,verbose_name="記事")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="ログイン名")
    text = models.TextField(verbose_name="投稿内容")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    class Meta:
        ordering = ['-created_date']


# Create your models here.

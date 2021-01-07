from django import forms
from PIL import Image
from django.forms import ModelForm
from .models import Product, Comment
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, label='ユーザー名')
    enter_password = forms.CharField(widget=forms.PasswordInput, label='パスワード')
    retype_password = forms.CharField(
        widget=forms.PasswordInput, label='再度パスワード')
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('このユーザー名はすでに使用されています')
        return username

    def clean_enter_password(self):
        password = self.cleaned_data.get('enter_password')
        if len(password) < 5:
            raise forms.ValidationError('パスワードは5文字以上入力する必要があります')
        return password

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('enter_password')
        retyped = self.cleaned_data.get('retype_password')
        if password and retyped and (password != retyped):
            self.add_error('retype_password', 'パスワードが一致しませんもう一度入力してください')

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('enter_password')
        new_user = User.objects.create_user(username=username)
        new_user.set_password(password)
        new_user.save()

    def __str__(self):
        return self.username


class ProductForm(forms.Form):
    Title = forms.CharField(label='タイトル', max_length=50,
                            widget=forms.TextInput, required=True)
    Price = forms.IntegerField(label='金額', required=True)
    Explanation = forms.CharField(
        label='商品の説明', max_length=100, widget=forms.TextInput, required=True)
    CHOICES = (
        ('朝飯', '朝飯'),
        ('おかず', 'おかず'),
        ('主食', '主食'),
        ('おつまみ', 'おつまみ'), 
        ('その他', 'その他'),
    )
    Choices = forms.ChoiceField(label='カテゴリー', choices=CHOICES, required=True)
#   Image = forms.ImageField(label='商品の画像')

    def clean_Price(self):
        Price = self.cleaned_data.get('Price')
        if Price < 1:
            raise forms.ValidationError('１円以上で入力してください')
        return Price

    def save(self):
        data = self.cleaned_data
        product = Product(title=data['Title'],
                          Price=data['Price'],
                          Explanation=data['Explanation'],
                          Choices=data['Choices'])
        product.save()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'Price', 'Explanation', 'Choices', 'Image')

    def clean_Price(self):
        Price = self.cleaned_data.get('Price')
        if Price < 1:
            raise forms.ValidationError('１円以上で入力してください')
        return Price


class CardForm(forms.Form):
    card = forms.CharField(label='カード情報', max_length=50,
                           widget=forms.TextInput, required=True)

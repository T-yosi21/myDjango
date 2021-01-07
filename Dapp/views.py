from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView,CreateView
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import *




def ProductDetail(request, pk):
    objects = Product.objects.get(pk=pk)
    comments = Comment.objects.filter(post=objects)
    form = CommentForm(request.POST)
    if form.is_valid(): 
            comment = form.save(commit=False) 
            comment.post = objects
            comment.author = request.user
            comment.save() 
    else:
        form = CommentForm()
    return render(request, 'detail.html', {
        'objects': objects,
        'form': form,
        'comments': comments
    }) 


# 確定！バリディー適応！！！
def ProductCreate(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dapp:ProductList')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'create.html', context)


# 確定！バリデーションの適応無し(自由に変更OK)！
class ProductUpdate(UpdateView):
    template_name = 'update.html'
    model = Product
    fields = ['title', 'Price', 'Explanation','Choices']
 
    def get_success_url(self):
        return reverse('Dapp:ProductList')
# @require_POST


def ProductDelete(request, pk):
    p = get_object_or_404(Product, id=pk)
    p.delete()
    return redirect('Dapp:ProductList')

# 確定（フロント側も確定！）
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dapp:ProductList')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

@login_required
# ログイン時のみ有効
def ProductList(request):
    object_lists = Product.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'object_lists': object_lists})

def article(request, pk):
    article = Product.objects.get(id=pk)
    comments = Comment.objects.filter(post=article)
    if request.method == "POST": 
        form = CommentForm(request.POST)
        if form.is_valid(): 
            comment = form.save(commit=False) 
            comment.post = article
            comment.author = request.user
            comment.save() 
    else:
        form = CommentForm()
    return render(request, 'index.html', {
        'article': article,
        'form': form,
        'comments': comments
    }) 


# Create your views here.
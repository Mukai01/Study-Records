from django.shortcuts import render

# 以下のコードを追加
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BlogModel
# Createの遷移の設定のために必要
from django.urls import reverse_lazy

# BlogListがListViewを継承
class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

# BlogDetailがDetailViewを継承
class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

# BlogCreateを定義
class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    # CreateViewの場合はmodelのどの項目を表示させるかを明示する
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list') #urls.pyでlistという名前を付けた

# BlogUpdateを追加
class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')
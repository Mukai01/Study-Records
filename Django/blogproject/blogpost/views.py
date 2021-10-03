from django.shortcuts import render

# 以下のコードを追加
from django.views.generic import ListView, DetailView
from .models import BlogModel

# BlogListがListViewを継承
class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

# BlogDetailがDetailViewを継承
class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel
from django.shortcuts import render

# 以下のコードを追加
from django.views.generic import ListView
from .models import BlogModel

# BlogListがListViewを継承
class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

from django.shortcuts import render
#import文を追加
from django.http import HttpResponse

def helloworldfunc(request):
    return HttpResponse('hello world')

from django.contrib import admin
# import 文を追加
from .models import SampleModel, BlogModel

# Modelを登録する
admin.site.register(SampleModel)
admin.site.register(BlogModel)
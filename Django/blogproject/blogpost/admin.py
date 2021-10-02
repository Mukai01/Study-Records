from django.contrib import admin
# import 文を追加
from .models import SampleModel

# Modelを登録する
admin.site.register(SampleModel)

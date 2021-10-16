from django.contrib import admin
from .models import ReviewModel

# 管理画面にReviewModelを表示するように変更
admin.site.register(ReviewModel)



from django.db import models
# 以下のコードを追加
from django.contrib.auth.models import User

EVALUATION_CHOICES = {('良い','良い'),('悪い','悪い')}
class ReviewModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Djangoがデフォルトで用意しているUserテーブルを外部キーに使用
    # on_deleteで models.CASCADEとするとUserが削除されると関連するオブジェクトも削除される
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 画像の保存先はsettings.pyで指定した場所でよければブランクでOK
    images = models.ImageField(upload_to='')
    useful_review = models.IntegerField(null=True, blank=True, default=0)
    useful_review_record = models.TextField()
    evaluation = models.CharField(max_length=10, choices=EVALUATION_CHOICES)
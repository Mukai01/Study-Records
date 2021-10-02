from django.db import models

# 以下のように追加する
class SampleModel(models.Model): # SampleMpdelは自由につけてよい
    title = models.CharField(max_length=100) # 最大100文字の文字列
    number = models.IntegerField() # 整数型のデータ

from django.db import models
# 左側がpythonの実装に使う表記、右が人間が見る表記
CATEGORY = (('business','ビジネス'),('life','生活'),('other','その他'))

# model.Modelを継承
class BlogModel(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField() # 長いときはTextField
    postdate = models.DateField(auto_now_add=True) # ブログ記事が投稿された日付を自動で記録
    category = models.CharField(max_length=50, choices = CATEGORY) # choicesでドロップダウン

    # 以下を追加
    # __str__ はオブジェクトの文字列表現を返す
    # BlogModelというクラスから作成された個別のオブジェクトに、self.titleという文字列表現を与える
    # これによりtitleが表示されるようになる
    def __str__(self):
        return self.title

# 過去に作成したコード
class SampleModel(models.Model): # SampleMpdelは自由につけてよい
    title = models.CharField(max_length=100) # 最大100文字の文字列
    number = models.IntegerField() # 整数型のデータ

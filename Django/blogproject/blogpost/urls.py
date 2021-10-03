# 以下のコードを追加
from django.urls import path
from .views import BlogList, BlogDetail

# requestにurlとあると、BlogListとして定義されたviewを呼び出す
# BlogDetailも追加する
# <int:pk>と書く
urlpatterns = [
    path('list/', BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view()),
]

# 初期設定の際に書いていたもの
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
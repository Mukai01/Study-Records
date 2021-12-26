from django.contrib import admin
from django.urls import path, include
# import 文を追加
from .views import helloworldfunc
from .views import HelloWorldClass

# helloworldの行を追加する
# helloworldfuncは後程view.pyで定義する
# HelloWorldClassのas_view()メソッドを使う
# 一番下にどれにも該当しなかったとき、helloworldappを呼び出すように記述
urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworldurl/',helloworldfunc),
    path('helloworldurl2/',HelloWorldClass.as_view()),
    path('', include('helloworldapp.urls')),
]

from django.contrib import admin
from django.urls import path
# import 文を追加
from .views import helloworldfunc
from .views import HelloWorldClass

# helloworldの行を追加する
# helloworldfuncは後程view.pyで定義する
# HelloWorldClassのas_view()メソッドを使う
urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworldurl/',helloworldfunc),
    path('helloworldurl2/',HelloWorldClass.as_view()),
]

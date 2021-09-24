from django.contrib import admin
from django.urls import path
# import 文を追加
from .views import helloworldfunc

# helloworldの行を追加する
# helloworldfuncは後程view.pyで定義する
urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworldurl/',helloworldfunc),
]
